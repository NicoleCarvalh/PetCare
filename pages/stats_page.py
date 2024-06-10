from PyQt5.QtWidgets import QTableWidgetItem, QPushButton, QMessageBox
from PyQt5.QtGui import *
from backend.routes import format_date, format_value
from backend.endpoints.sales import get_sales_list
from datetime import datetime, timedelta
from dateutil.parser import parse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Consumir API e informar dados nos blocos 
# Verificar gráficos


def sales_frame(self):
  sales_data = get_sales_list()
  
  sales_df = pd.DataFrame(sales_data)
  
  sales_df['date_time'] = pd.to_datetime(sales_df['date_time'])
  
  today = datetime.today().date()
  yesterday = today - timedelta(days=1)
  
  today_sales = sales_df[sales_df['date_time'].dt.date == today]
  yesterday_sales = sales_df[sales_df['date_time'].dt.date == yesterday]
  
  today_total = today_sales['total'].sum()
  yesterday_total = yesterday_sales['total'].sum()
  

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

def stock_frame(self):
  pass

def products_frame(self):
  pass

def clients_frame(self):
  pass

def populate_dashboard(self):
  sales_frame(self)
  