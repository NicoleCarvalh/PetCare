import requests
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from backend.endpoints.employees import get_employees_list

employees_data = ''

def populate_employees_table(self):
  self.employees_table.setColumnWidth(0, 90)
  self.employees_table.setColumnWidth(1, 310)
  self.employees_table.setColumnWidth(2, 350)
  self.employees_table.setColumnWidth(3, 350)
  self.employees_table.setColumnWidth(4, 350)
  self.employees_table.setStyleSheet(
    "alternate-background-color: #F8E7BB;"
    "background-color: white;"
  )

  employees_data = get_employees_list()

  row_count = len(employees_data)

  self.employees_table.setRowCount(row_count)

  for row, employee in enumerate(employees_data):
    self.employees_table.setItem(row, 0, QTableWidgetItem(str(employee['id'])))

    image_url = employee['avatar_url']

    if image_url == None:
      image_item = QTableWidgetItem()
      icon = QIcon(QPixmap('resources/icons/user.svg'))  
      image_item.setIcon(icon)
      self.employees_table.setItem(row, 1, image_item)

    else:
      image_data = requests.get(image_url).content
      with open("downloaded_image.png", "wb") as handler:
        handler.write(image_data)

      image_item = QTableWidgetItem()
      icon = QIcon(QPixmap("downloaded_image.png"))
      image_item.setIcon(icon)
      image_item.setTextAlignment(Qt.AlignCenter)
      self.employees_table.setItem(row, 1, image_item)

    self.employees_table.setItem(row, 2, QTableWidgetItem(str(employee['name'])))
    self.employees_table.setItem(row, 3, QTableWidgetItem(str(employee['role'])))
    self.employees_table.setItem(row, 4, QTableWidgetItem(str(employee['email'])))
    