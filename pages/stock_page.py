from PyQt5.QtWidgets import QTableWidgetItem
from backend.endpoints.products import get_products_list

#TODO arrumar status estoque
#TODO arrumar listagem de imagens

stock_data = ''
product_status = ''

def populate_stock_table(self):
  self.stock_table.setColumnWidth(0, 90)
  self.stock_table.setColumnWidth(1, 100)
  self.stock_table.setColumnWidth(2, 100)
  self.stock_table.setColumnWidth(3, 100)
  self.stock_table.setColumnWidth(4, 100)
  self.stock_table.setColumnWidth(5, 100)
  self.stock_table.setColumnWidth(6, 100)
  self.stock_table.setColumnWidth(7, 100)
  self.stock_table.setColumnWidth(8, 100)
  self.stock_table.setColumnWidth(9, 100)
  self.stock_table.setStyleSheet(
    "alternate-background-color: #F8E7BB;"
    "background-color: white;"
  )

  stock_data = get_products_list()
  # print(stock_data)

  row_count = len(stock_data)
  # print(row_count)

  self.stock_table.setRowCount(row_count)

  for row, product in enumerate(stock_data):
    self.stock_table.setItem(row, 0, QTableWidgetItem(str(product['id'])))
    self.stock_table.setItem(row, 1, QTableWidgetItem(str(product['code'])))
    self.stock_table.setItem(row, 2, QTableWidgetItem(str(product['image_url'])))
    self.stock_table.setItem(row, 3, QTableWidgetItem(str(product['name'])))
    self.stock_table.setItem(row, 4, QTableWidgetItem(str(product['description'])))
    self.stock_table.setItem(row, 5, QTableWidgetItem(str(product['quantity_in_stock'])))
    self.stock_table.setItem(row, 6, QTableWidgetItem(str(product['sale_price'])))
    self.stock_table.setItem(row, 7, QTableWidgetItem(str(product['purchase_price'])))
    self.stock_table.setItem(row, 8, QTableWidgetItem(str(product['last_refill'])))


    # if product['quantity_in_stock'] < 10:
    #   product_status = "Esgotado"
    #   return product_status
    # elif product['quantity_in_stock'] >= 10:
    #   product_status = "Escasso"
    #   return product_status
    # elif product['quantity_in_stock'] >= 30:
    #   product_status = "Cheio"
    #   return product_status

    # self.stock_table.setItem(row, 9, QTableWidgetItem(str(product_status)))
    