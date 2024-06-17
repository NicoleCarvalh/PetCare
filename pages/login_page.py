from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
from backend.endpoints.employees import verify_credentials
from pages.dashboard_page import DashboardPage

class LoginPage(QDialog):
  def __init__(self, widget):
    super(LoginPage, self).__init__()
    uic.loadUi("layouts/login.ui", self)
    self.widget = widget
    self.set_fonts()

    self.login_button.clicked.connect(self.login) 
    self.email_input.returnPressed.connect(self.login)
    self.password_input.returnPressed.connect(self.login)

    self.loading_bar.setVisible(False)

  def keyPressEvent(self, event: QKeyEvent):
    if event.key() == Qt.Key_Escape:
        event.ignore()
    else:
        super().keyPressEvent(event)

  def set_fonts(self):
    font_path = 'resources/fonts/Inter/Inter.ttf'
    QFontDatabase.addApplicationFont(font_path)
    inter_font_family = 'Inter'

    title_font = QFont(inter_font_family, 17)
    label_font = QFont(inter_font_family, 14)
    button_font = QFont(inter_font_family, 12)
    button_font.setWeight(500)
    link_font = QFont(inter_font_family, 11)
    link_font.setUnderline(True)
    validation_font = QFont(inter_font_family, 11)

    self.greetings.setFont(title_font)  
    self.email_label.setFont(label_font)  
    self.password_label.setFont(label_font)  
    self.login_button.setFont(button_font)  
    self.forgot_password.setFont(link_font)  
    self.register_label.setFont(link_font)  
    self.validation_text.setFont(validation_font)

  def login(self):
    email = self.email_input.text()
    password = self.password_input.text()

    self.validation_text.setText(" ")

    self.loading_bar.setVisible(True)
    self.loading_bar.setValue(0)

    if len(email) == 0 or len(password) == 0:
      self.validation_text.setText("Por favor, preencha todos os campos.")
      self.loading_bar.setVisible(False)  
      return

    response = verify_credentials(email, password)

    if response:
      self.validation_text.setText('')
      self.email_input.clear()
      self.password_input.clear()
      self.loading_bar.setValue(100)
      self.go_to_dashboard()
    else:
      self.validation_text.setText("E-mail ou senha incorretos.")

    QTimer.singleShot(1000, lambda: self.loading_bar.setVisible(False))
    QTimer.singleShot(3000, lambda: self.validation_text.setText(""))
    
  def go_to_dashboard(self):
    dashboard = DashboardPage(self.widget)
    self.widget.addWidget(dashboard)
    self.widget.setCurrentIndex(self.widget.currentIndex() + 1)
