from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5 import uic
from PyQt5.QtGui import QKeyEvent
# from pages.sales_page import SalesPage
from pages.sales_page import populate_sales_table

class DashboardPage(QDialog):
  def __init__(self, widget):
    super(DashboardPage, self).__init__()
    uic.loadUi("layouts/dashboard.ui", self)

    self.widget = widget

    self.full_menu.hide()
    self.dashboard_btn_2.setChecked(True)
    self.exit_btn_1.clicked.connect(self.exit_to_login)
    self.exit_btn_2.clicked.connect(self.exit_to_login)

    populate_sales_table(self)

  def keyPressEvent(self, event: QKeyEvent):
    if event.key() == Qt.Key_Escape:
      event.ignore()
    else:
      # Allow default 
      super().keyPressEvent(event)

  def exit_to_login(self):
    self.widget.setCurrentIndex(0)


  def on_dashboard_btn_1_toggled(self):
    self.stackedWidget.setCurrentIndex(0)
    self.page_title.setText("Dashboard")
    self.search_input.hide()
    self.search_btn.hide()

  def on_dashboard_btn_2_toggled(self):
    self.stackedWidget.setCurrentIndex(0)
    self.page_title.setText("Dashboard")
    self.search_input.hide()
    self.search_btn.hide()
    

  def on_employees_btn_1_toggled(self):
    self.stackedWidget.setCurrentIndex(1)
    self.page_title.setText("Funcionários")
    self.search_input.show()
    self.search_btn.show()

  def on_employees_btn_2_toggled(self):
    self.stackedWidget.setCurrentIndex(1)
    self.page_title.setText("Funcionários")
    self.search_input.show()
    self.search_btn.show()


  def on_stock_btn_1_toggled(self):
    self.stackedWidget.setCurrentIndex(2)
    self.page_title.setText("Estoque")
    self.search_input.show()
    self.search_btn.show()

  def on_stock_btn_2_toggled(self):
    self.stackedWidget.setCurrentIndex(2)
    self.page_title.setText("Estoque")
    self.search_input.show()
    self.search_btn.show()


  def on_clients_btn_1_toggled(self):
    self.stackedWidget.setCurrentIndex(3)
    self.page_title.setText("Clientes")
    self.search_input.show()
    self.search_btn.show()

  def on_clients_btn_2_toggled(self):
    self.stackedWidget.setCurrentIndex(3)
    self.page_title.setText("Clientes")
    self.search_input.show()
    self.search_btn.show()


  def on_sales_btn_1_toggled(self):
    self.stackedWidget.setCurrentIndex(4)

    # populate_sales_table(self)

  def on_sales_btn_2_toggled(self):
    self.stackedWidget.setCurrentIndex(4)

    # populate_sales_table(self)