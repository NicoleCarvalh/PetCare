from PyQt5.QtWidgets import QTableWidgetItem, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from backend.routes import format_date, format_value
from backend.endpoints.sales import get_sales_list

#TODO arrumar listagem de produtos

sales_data = ''

def populate_sales_table(self):
  def view_items(row):
    
    sale_id = int(self.sales_table.item(row, 0).text())

    sale = sales_data[row]

    items_details = []

    for item in sale['products']:
      product_id = item['product_id']

      product_name = item['product']['name']
      quantity = item['quantity']
      
      price = item['product']['sale_price']
      items_details.append(f"\n ID: {product_id} - {product_name} - {quantity} unidades - R${price:.2f}")

    items_text = "\n".join(items_details)
    
    items_dialog = QMessageBox()
    items_dialog.setWindowIcon(QIcon('resources/images/DesktopIcon.png'))
    items_dialog.setWindowTitle("Itens da Venda")
    items_dialog.setText(f"Itens da Venda ID {sale_id}:\n{items_text}")
    items_dialog.exec_()


  self.sales_table.setColumnWidth(0, 80)
  self.sales_table.setColumnWidth(1, 290)
  self.sales_table.setColumnWidth(2, 270)
  self.sales_table.setColumnWidth(3, 250)
  self.sales_table.setColumnWidth(4, 270)
  self.sales_table.setColumnWidth(5, 220)

  sales_data = get_sales_list()

  row_count = len(sales_data)

  self.sales_table.setRowCount(row_count)

  for row, sale in enumerate(sales_data):

    self.sales_table.setItem(row, 0, QTableWidgetItem(str(sale['id'])))
    self.sales_table.setItem(row, 1, QTableWidgetItem(str(sale['client']['name'])))
    self.sales_table.setItem(row, 2, QTableWidgetItem(format_date(sale['date_time'])))
    self.sales_table.setItem(row, 3, QTableWidgetItem(format_value(sale['total'])))
    self.sales_table.setItem(row, 4, QTableWidgetItem(str(sale['payment_method'])))

    btn_view_items = QPushButton("Ver Itens")
    btn_view_items.clicked.connect(lambda _, row=row: view_items(row))
    self.sales_table.setCellWidget(row, 5, btn_view_items)
