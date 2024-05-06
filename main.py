from PyQt5.QtWidgets import QApplication, QDialog, QLabel
from PyQt5.QtCore import pyqtSlot, QFile, QTextStream, QUrl
from PyQt5.QtGui import QIcon, QFont, QFontDatabase, QDesktopServices
from PyQt5 import uic, QtWidgets
from api import verify_credentials
import sys

# from PyQt5.QtWidgets import QFrame, QLabel, QLineEdit, QMessageBox, QWidget, QPushButton, QMainWindow
# from dotenv import load_dotenv
# from PyQt5.uic import loadUi
# import requests

#TODO design the pages left

class Main(QDialog):
  def __init__(self):
    super(Main, self).__init__()
    
    # Load the Login UI file
    uic.loadUi("screens/login.ui", self)

    # Set font sizes
    self.set_fonts()

    self.login_button.clicked.connect(self.go_to_dashboard) #TODO alterar a função para "login" para deploy // go_to_dashboard para desenvolvimento

    # Set Enter keyboard button to login
    self.email_input.returnPressed.connect(self.go_to_dashboard)
    self.password_input.returnPressed.connect(self.go_to_dashboard)


    #TODO adicionar links da página de login


  def set_fonts(self):
    ################ FONTS ##################
    # Insert the font into the font database
    font_path = 'resources/fonts/Inter/Inter.ttf'
    QFontDatabase.addApplicationFont(font_path)
    inter_font_family = 'Inter'

    # Set font sizes
    title_font = QFont(inter_font_family, 17)
    label_font = QFont(inter_font_family, 14)
    button_font = QFont(inter_font_family, 12)
    button_font.setWeight(500)
    link_font = QFont(inter_font_family, 11)
    link_font.setUnderline(True)
    validation_font = QFont(inter_font_family, 11)

    # Change font for specific widgets
    self.greetings.setFont(title_font)  
    self.email_label.setFont(label_font)  
    self.password_label.setFont(label_font)  
    self.login_button.setFont(button_font)  
    self.forgot_password.setFont(link_font)  
    self.register_label.setFont(link_font)  
    self.validation_text.setFont(validation_font)
    #########################################

  def login(self):
    email = self.email_input.text()
    password = self.password_input.text()

    if len(email) == 0 or len(password) == 0:
      self.validation_text.setText("Por favor, preencha todos os campos.")
      return

    response = verify_credentials(email, password)

    if response:
      self.go_to_dashboard()
    else:
      self.validation_text.setText("E-mail ou senha incorretos.")

  # Load the Dashboard UI file
  def go_to_dashboard(self):
    dashboard = Dashboard()
    widget.addWidget(dashboard)
    widget.setCurrentIndex(widget.currentIndex()+1)

class Dashboard(QDialog):
  def __init__(self):
    super(Dashboard, self).__init__()
    uic.loadUi("screens/dashboard.ui", self)
    # uic.loadUi("screens/dashboard-MainWindow.ui", self)
    self.full_menu.hide()
    self.dashboard_btn_2.setChecked(True)
    self.exit_btn_1.clicked.connect(self.exit_to_login)

  def exit_to_login(self):
    widget.setCurrentIndex(0)

  # Function for searching
  def search(self):
    self.stackedWidget.setCurrentIndex(5)
    search_text = self.search_input.text().strip()
    if search_text:
      self.label_6.setText(search_text)

  
  # # Changing page to user page
  # def on_user_btn_clicked(self):
  #   self.stackedWidget.setCurrentIndex(6)

  # Changing PushButton checkable status when stackedWidget index change
  # def on_stackedWidget_currentChanged(self, index):
  #   btn_list = self.icon_only_menu.findChildren(QPushButton) \
  #   + self.icon_only_menu.findChildren(QPushButton)

  #   for btn in btn_list:
  #     if index in [5, 6]:
  #       btn.setAutoExclusive(False)
  #       btn.setChecked(False)
  #     else:        
  #       btn.setAutoExclusive(True)

  # Changing menu pages
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

  #   self.setStyleSheet(
  #     "QDialog {"
  #     "background-color: white;"
  #     "}"
  #     "QTableWidget {"
  #     "border-radius: 10px;"
  #     "background-color: black;"
  #     "}"
  #     "QTableWidget::item {"
  #     "border-bottom: 1px solid gray;"
  #     "}"
  #     "QTableWidget::item:selected {"
  #     "background-color: #b7cde0;" # Altere essa cor para a cor de seleção desejada
  #     "}"
  #     "QHeaderView::section {"
  #     "border-radius: 10px;"
  #     "background-color: #d3d3d3;" # Cor de fundo do cabeçalho
  #     "}"
  # )

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
    
  
# Initialize App
if __name__ == "__main__":
  app = QApplication(sys.argv)

  window = Main()
  widget = QtWidgets.QStackedWidget()
  widget.addWidget(window)
  widget.setFixedHeight(1000)
  widget.setFixedWidth(1600)
  widget.setWindowIcon(QIcon('resources/images/DesktopIcon.png'))
  widget.setWindowTitle("PetCare Connect")
  widget.show()
  sys.exit(app.exec_())