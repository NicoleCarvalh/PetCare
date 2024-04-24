from PyQt5.QtWidgets import QApplication, QDialog, QFrame, QLabel, QLineEdit, QMessageBox
from PyQt5 import uic
from PyQt5.QtGui import QIcon, QFont, QFontDatabase
from PyQt5.QtCore import pyqtSlot, QFile, QTextStream
from dotenv import load_dotenv
import requests
import sys
from api import verify_credentials

#TODO design the pages left

class Main(QDialog):
  def __init__(self):
    super(Main, self).__init__()
    
    # Load the Login UI file
    uic.loadUi("screens/login.ui", self)
    
    # Set window Icon and Title
    self.setWindowTitle("PetCare Connect")
    self.setWindowIcon(QIcon('resources/images/DesktopIcon.png'))
    self.login_button.clicked.connect(self.login)

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
    if response.status_code == 200:
      self.load_dashboard()
    else:
      self.validation_text.setText("E-mail ou senha incorretos.")

  # Load the Dashboard UI file
  def load_dashboard(self):
    uic.loadUi("screens/dashboard.ui", self) 
    self.show()

# Initialize App
if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = Main()
  window.show()
  app.exec_()