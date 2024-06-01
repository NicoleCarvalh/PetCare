from PyQt5.QtWidgets import QTableWidgetItem
from backend.endpoints.employees import get_employees_list

#TODO arrumar listagem de imagens

employees_data = ''

def populate_employees_table(self):
  self.employees_table.setColumnWidth(0, 90)
  self.employees_table.setColumnWidth(1, 310)
  self.employees_table.setColumnWidth(2, 300)
  self.employees_table.setColumnWidth(3, 280)
  self.employees_table.setColumnWidth(4, 290)
  self.employees_table.setStyleSheet(
    "alternate-background-color: #F8E7BB;"
    "background-color: white;"
  )

  employees_data = get_employees_list()

  row_count = len(employees_data)

  self.employees_table.setRowCount(row_count)

  for row, employee in enumerate(employees_data):
    self.employees_table.setItem(row, 0, QTableWidgetItem(str(employee['id'])))
    self.employees_table.setItem(row, 1, QTableWidgetItem(str(employee['avatar_url'])))
    self.employees_table.setItem(row, 2, QTableWidgetItem(str(employee['name'])))
    self.employees_table.setItem(row, 3, QTableWidgetItem(str(employee['role'])))
    self.employees_table.setItem(row, 4, QTableWidgetItem(str(employee['email'])))
    