from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
from PyQt5.QtGui import QIcon, QFont, QFontDatabase
from PyQt5 import uic, QtWidgets
from api import verify_credentials
import sys


# from PyQt5.QtWidgets import QFrame, QLabel, QLineEdit, QMessageBox, QWidget
# from PyQt5.QtCore import pyqtSlot, QFile, QTextStream
# from dotenv import load_dotenv
# from PyQt5.uic import loadUi
# import requests

#TODO design the pages left

class Main(QDialog):
  def __init__(self):
    super(Main, self).__init__()
    
    # Load the Login UI file
    uic.loadUi("screens/login.ui", self)

    self.login_button.clicked.connect(self.goToDashboard) #TODO alterar a função para "login" para deploy

    # Set Enter keyboard button to login
    self.email_input.returnPressed.connect(self.goToDashboard)
    self.password_input.returnPressed.connect(self.goToDashboard)

    # Set font sizes
    self.setFonts()

  def setFonts(self):
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
      self.goToDashboard()
    else:
      self.validation_text.setText("E-mail ou senha incorretos.")

  # Load the Dashboard UI file
  def goToDashboard(self):
    dashboard = Dashboard()
    widget.addWidget(dashboard)
    widget.setCurrentIndex(widget.currentIndex()+1)

class Dashboard(QDialog):
  def __init__(self):
    super(Dashboard, self).__init__()
    uic.loadUi("screens/dashboard.ui", self)
    # uic.loadUi("screens/dashboard-MainWindow.ui", self)
    self.icon_only_menu.hide()
    self.dashboard_btn_2.setChecked(True)

# Initialize App
if __name__ == "__main__":
  app = QApplication(sys.argv)

  # Loading style file
  with open("style.qss", "r") as style_file:
    style_str = style_file.read()

  app.setStyleSheet(style_str)

  window = Main()
  widget = QtWidgets.QStackedWidget()
  widget.addWidget(window)
  widget.setFixedHeight(1000)
  widget.setFixedWidth(1600)
  widget.setWindowIcon(QIcon('resources/images/DesktopIcon.png'))
  widget.setWindowTitle("PetCare Connect")
  widget.show()
  sys.exit(app.exec_())