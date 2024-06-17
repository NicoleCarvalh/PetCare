from PyQt5.QtWidgets import QVBoxLayout, QTableWidgetItem
from PyQt5.QtGui import *
from backend.routes import format_value, format_date
from backend.endpoints.sales import get_sales_list
from backend.endpoints.clients import get_clients_list
from backend.endpoints.products import get_products_list
from datetime import datetime, timedelta
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import pandas as pd


def sales_frame(self):
  plt.rcParams['font.family'] = 'Poppins'

  sales_data = get_sales_list()
  
  sales_df = pd.DataFrame(sales_data)
  
  sales_df['date_time'] = pd.to_datetime(sales_df['date_time'])
  
  # Sales comparison 
  today = datetime.today().date()
  yesterday = today - timedelta(days=1)
  
  today_sales = sales_df[sales_df['date_time'].dt.date == today]
  yesterday_sales = sales_df[sales_df['date_time'].dt.date == yesterday]
  
  today_total = today_sales['total'].sum()
  yesterday_total = yesterday_sales['total'].sum()

  # Sales mean Dashboard frame
  sales_mean = sales_df['total'].mean()

  # Products sold
  exploded_sales = sales_df.explode('products')

  products_df = pd.json_normalize(exploded_sales['products'])

  quantity_sold = products_df.groupby('product_id')['quantity'].sum().reset_index()
  
  total_products_sold = quantity_sold['quantity'].sum()

  # NAN verification
  if today_total > yesterday_total:
    if yesterday_total != 0:
      percentage = ((today_total - yesterday_total) / yesterday_total) * 100
    else:
      percentage = 100
    
    comparison = f'+ {percentage:.2f}% que ontem'
    self.sales_comparison.setText(comparison)
    self.sales_comparison.setStyleSheet(
      "color: #4079ED;" 
    )
    
  elif today_total == yesterday_total:
    self.sales_comparison.setText('O mesmo que ontem')
    self.sales_comparison.setStyleSheet(
      "color: #CD6200;" 
    )
  else:
    if yesterday_total != 0:
      percentage = ((today_total - yesterday_total) / yesterday_total) * 100
    else:
      percentage = 100
    
    comparison = f'{percentage:.2f}% que ontem'
    self.sales_comparison.setText(comparison)
    self.sales_comparison.setStyleSheet(
      "color: #A30D11;" 
    )

  self.sales_count.setText(format_value(today_total))
  self.sales_mean_count.setText(format_value(sales_mean))
  self.products_count.setText(str(total_products_sold))

  # Main chart
  figure = Figure(figsize=(1, 1), facecolor='none') 
  canvas = FigureCanvas(figure)
  ax = figure.add_subplot(111, facecolor='none')

  ax.bar(['Ontem', 'Hoje'], [yesterday_total, today_total], color=['#FF5733', '#33FF57'])
  ax.set_title('Comparação de Vendas')
  ax.set_ylabel('Total de Vendas')

  ax.patch.set_alpha(0.0)
  figure.patch.set_alpha(0.0)

  main_chart_layout = QVBoxLayout()
  main_chart_layout.addWidget(canvas)
  self.main_chart.setLayout(main_chart_layout)

  # Most sold products 
  top5_products_df = quantity_sold.nlargest(10, 'quantity')

  top5_products_df = top5_products_df.sort_values(by='quantity', ascending=False)

  self.table1.setRowCount(len(top5_products_df))
  self.table1.setColumnCount(2)
  self.table1.setHorizontalHeaderLabels(['ID Produto', 'Quantidade Vendida'])
  self.table1.setColumnWidth(0, 320)
  self.table1.setColumnWidth(1, 320)

  for i, row in top5_products_df.iterrows():
    product_id_item = QTableWidgetItem(str(row['product_id']))
    quantity_sold_item = QTableWidgetItem(str(row['quantity']))
    self.table1.setItem(i, 0, product_id_item)  
    self.table1.setItem(i, 1, quantity_sold_item)  


def clients_frame(self):
  clients_data = get_clients_list()

  clients_quantity = 0

  for client in clients_data:
    clients_quantity += 1
  
  self.client_count.setText(str(clients_quantity))


def products_frame(self):
  products_data = get_products_list()  
  products_df = pd.DataFrame(products_data)
  low_stock_df = products_df[products_df['quantity_in_stock'] < 30] 

  self.table2.setRowCount(len(low_stock_df))
  self.table2.setColumnCount(4)
  self.table2.setHorizontalHeaderLabels(['ID Produto', 'Nome', 'Quantidade em Estoque', 'Última Reposição'])
  self.table2.setColumnWidth(0, 100)
  self.table2.setColumnWidth(1, 250)
  self.table2.setColumnWidth(2, 150)
  self.table2.setColumnWidth(3, 150)

  for i, row in enumerate(low_stock_df.itertuples(), start=0):
    product_id_item = QTableWidgetItem(str(row.id))
    name_item = QTableWidgetItem(row.name)
    quantity_item = QTableWidgetItem(str(row.quantity_in_stock))
    last_refill_item = QTableWidgetItem(format_date(row.last_refill))

    self.table2.setItem(i, 0, product_id_item)
    self.table2.setItem(i, 1, name_item)
    self.table2.setItem(i, 2, quantity_item)
    self.table2.setItem(i, 3, last_refill_item)


def populate_dashboard(self):
  sales_frame(self)
  clients_frame(self)
  products_frame(self)