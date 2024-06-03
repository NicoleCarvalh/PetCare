from PyQt5.QtWidgets import QTableWidgetItem
from backend.endpoints.products import get_products_list
from backend.routes import format_date, format_value
from backend.routes import check_status
from PyQt5.QtGui import *

stock_data = ''
product_status = ''

def populate_stock_table(self):
  inter_font_path = 'resources/fonts/Inter/Inter.ttf'
  montserrat_font_path = 'resources/fonts/Montserrat/static/Montserrat-Medium.ttf'
  QFontDatabase.addApplicationFont(inter_font_path)
  QFontDatabase.addApplicationFont(montserrat_font_path)

  inter_font_family = 'Inter'
  montserrat_font_family = 'MontserratM'

  header_font = QFont(inter_font_family, 11)
  header_font.setWeight(500)
  text_font = QFont(montserrat_font_family, 11)

  for i in range(9):
    self.stock_table.horizontalHeaderItem(i).setFont(header_font) 

  self.stock_table.setFont(text_font)

  self.stock_table.setColumnWidth(0, 90)
  self.stock_table.setColumnWidth(1, 150)
  self.stock_table.setColumnWidth(2, 300)
  self.stock_table.setColumnWidth(3, 120)
  self.stock_table.setColumnWidth(4, 150)
  self.stock_table.setColumnWidth(5, 160)
  self.stock_table.setColumnWidth(6, 220)
  self.stock_table.setColumnWidth(7, 180)
  self.stock_table.setColumnWidth(8, 400)
  self.stock_table.setStyleSheet(
    "alternate-background-color: #F8E7BB;"
    "background-color: white;"
  )

  stock_data = get_products_list()

  row_count = len(stock_data)

  self.stock_table.setRowCount(row_count)

  for row, product in enumerate(stock_data):
    self.stock_table.setItem(row, 0, QTableWidgetItem(str(product['id'])))
    self.stock_table.setItem(row, 1, QTableWidgetItem(str(product['code'])))
    self.stock_table.setItem(row, 2, QTableWidgetItem(str(product['name'])))
    self.stock_table.setItem(row, 3, QTableWidgetItem(str(product['quantity_in_stock'])))
    self.stock_table.setItem(row, 4, QTableWidgetItem(format_value(product['sale_price'])))
    self.stock_table.setItem(row, 5, QTableWidgetItem(format_value(product['purchase_price'])))
    self.stock_table.setItem(row, 6, QTableWidgetItem(format_date(product['last_refill'])))

    self.stock_table.setItem(row, 7, QTableWidgetItem(check_status(product['quantity_in_stock'])))
    self.stock_table.setItem(row, 8, QTableWidgetItem(str(product['description'])))

    self.stock_table.setRowHeight(row, 70)

