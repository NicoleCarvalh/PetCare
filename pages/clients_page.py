from PyQt5.QtWidgets import QTableWidgetItem
from backend.endpoints.clients import get_clients_list
from datetime import date
from PyQt5.QtGui import *

def populate_clients_table(self):
  inter_font_path = 'resources/fonts/Inter/Inter.ttf'
  montserrat_font_path = 'resources/fonts/Montserrat/static/Montserrat-Medium.ttf'
  QFontDatabase.addApplicationFont(inter_font_path)
  QFontDatabase.addApplicationFont(montserrat_font_path)

  inter_font_family = 'Inter'
  montserrat_font_family = 'MontserratM'

  header_font = QFont(inter_font_family, 11)
  header_font.setWeight(500)
  text_font = QFont(montserrat_font_family, 11)

  for i in range(6):
    self.clients_table.horizontalHeaderItem(i).setFont(header_font) 

  self.clients_table.setFont(text_font)

  self.clients_table.setColumnWidth(0, 90)
  self.clients_table.setColumnWidth(1, 350)
  self.clients_table.setColumnWidth(2, 350)
  self.clients_table.setColumnWidth(3, 200)
  self.clients_table.setColumnWidth(4, 250)
  self.clients_table.setColumnWidth(5, 250)
  self.clients_table.setStyleSheet(
    "alternate-background-color: #F8E7BB;"
    "background-color: white;"
  )

  clients_data = get_clients_list()

  row_count = len(clients_data)

  self.clients_table.setRowCount(row_count)

  for row, client in enumerate(clients_data):
    self.clients_table.setItem(row, 0, QTableWidgetItem(str(client['id'])))
    self.clients_table.setItem(row, 1, QTableWidgetItem(str(client['name'])))
    self.clients_table.setItem(row, 2, QTableWidgetItem(str(client['email'])))
    self.clients_table.setItem(row, 3, QTableWidgetItem(client['birthday']))
    self.clients_table.setItem(row, 4, QTableWidgetItem(str(client['address']['city'])))
    self.clients_table.setItem(row, 5, QTableWidgetItem(str(client['address']['state'])))

    self.clients_table.setRowHeight(row, 70)