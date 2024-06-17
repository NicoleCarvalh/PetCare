from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QUrl
from PyQt5 import uic
from PyQt5.QtGui import QKeyEvent, QDesktopServices
from pages.sales_page import populate_sales_table
from pages.employees_page import populate_employees_table
from pages.clients_page import populate_clients_table
from pages.stock_page import populate_stock_table
from pages.stats_page import populate_dashboard
from layouts.report_layout import generate_pdf, fetch_report_data

class DashboardPage(QDialog):
  def __init__(self, widget):
    super(DashboardPage, self).__init__()
    uic.loadUi("layouts/dashboard.ui", self)

    self.widget = widget

    self.full_menu.hide()
    self.dashboard_btn_2.setChecked(True)
    self.exit_btn_1.clicked.connect(self.exit_to_login)
    self.exit_btn_2.clicked.connect(self.exit_to_login)

    populate_employees_table(self)
    populate_stock_table(self)
    populate_clients_table(self)
    populate_sales_table(self)
    populate_dashboard(self)

    self.export_btn.clicked.connect(self.open_pdf)

  def keyPressEvent(self, event: QKeyEvent):
    if event.key() == Qt.Key_Escape:
      event.ignore()
    else:
      # Allow default 
      super().keyPressEvent(event)

  def exit_to_login(self):
    self.widget.setCurrentIndex(0)

  def open_pdf(self):
    report_data = fetch_report_data()
    generate_pdf(report_data, filename="report.pdf")

    QDesktopServices.openUrl(QUrl.fromLocalFile("report.pdf"))


  def on_dashboard_btn_1_toggled(self):
    self.stackedWidget.setCurrentIndex(0)
    self.page_title.setText("Dashboard > Resumo diário")
    self.search_input.hide()
    self.search_btn.hide()

  def on_dashboard_btn_2_toggled(self):
    self.stackedWidget.setCurrentIndex(0)
    self.page_title.setText("Dashboard > Resumo diário")
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
    self.page_title.setText("Vendas")
    self.search_input.show()
    self.search_btn.show()

  def on_sales_btn_2_toggled(self):
    self.stackedWidget.setCurrentIndex(4)
    self.page_title.setText("Vendas")
    self.search_input.show()
    self.search_btn.show()