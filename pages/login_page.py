from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QFont, QFontDatabase
from PyQt5 import uic
from PyQt5.QtGui import QKeyEvent
from backend.endpoints.employees import verify_credentials
from pages.dashboard_page import DashboardPage

#TODO adicionar links da página de login
#TODO adicionar loader da página de login

class WorkerThread(QThread):
  finished = pyqtSignal(bool)  # Sinal para indicar que a tarefa foi concluída

  def __init__(self, email, password):
    super().__init__()
    self.email = email
    self.password = password

  def run(self):
    # Simular uma operação de verificação de credenciais
    result = verify_credentials(self.email, self.password)
    self.finished.emit(result)


class LoginPage(QDialog):
  def __init__(self, widget):
    super(LoginPage, self).__init__()
    uic.loadUi("layouts/login.ui", self)
    self.widget = widget
    self.set_fonts()

    #TODO alterar a função para "login" para deploy // go_to_dashboard para desenvolvimento

    self.login_button.clicked.connect(self.go_to_dashboard) 
    self.email_input.returnPressed.connect(self.go_to_dashboard)
    self.password_input.returnPressed.connect(self.go_to_dashboard)
    self.settings = QSettings("Empresa", "MeuApp")

    # self.login_button.clicked.connect(self.login) 
    # self.email_input.returnPressed.connect(self.login)
    # self.password_input.returnPressed.connect(self.login)
    # #maria.oliveira@example.com

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

    if len(email) == 0 or len(password) == 0:
      self.validation_text.setText("Por favor, preencha todos os campos.")
      return

    self.loading_bar.setVisible(True)
    self.loading_bar.setValue(0)

    # stored_response = self.settings.value("api_response", defaultValue=False)

    stored_email = self.settings.value("email")
    stored_password = self.settings.value("password")

    # Verificar se os dados da API estão armazenados e válidos
    if stored_email is not None and stored_password is not None:
      # Dados de login encontrados no armazenamento local, comparar com os fornecidos pelo usuário
      if email == stored_email and password == stored_password:
        # Login bem-sucedido localmente, ir para o dashboard
        self.loading_bar.setVisible(False)
        self.go_to_dashboard()
        return
      else:
        # Login local falhou, fazer login na API
        self.thread = WorkerThread(email, password)
        self.thread.finished.connect(self.on_login_finished)
        self.thread.start()
    else:
      # Não há dados de login armazenados localmente, fazer login na API
      self.thread = WorkerThread(email, password)
      self.thread.finished.connect(self.on_login_finished)
      self.thread.start()

  def verify_local_login(self, email, password):
    # Recuperar os dados da resposta da API
    stored_email = self.settings.value("email")
    stored_password = self.settings.value("password")
    expiration_date = self.settings.value("expiration_date")

    # Verificar se os dados armazenados estão presentes e não expirados
    if (stored_email == email and stored_password == password and expiration_date.isValid() and QDateTime.currentDateTime() < expiration_date):
        # Os dados armazenados são válidos
        return True
    else:
        # Os dados armazenados são inválidos ou expiraram
        return False

  def on_login_finished(self, result):
    if result:
      self.validation_text.setText('')
      self.email_input.clear()
      self.password_input.clear()
      
      # Armazenar os dados da resposta da API
      self.settings.setValue("api_response", True)
      
      # Definir a data de expiração como 7 dias após o login
      expiration_date = QDateTime.currentDateTime().addDays(7)
      self.settings.setValue("expiration_date", expiration_date)
      
      self.go_to_dashboard()
    else:
      self.validation_text.setText("E-mail ou senha incorretos.")

    self.loading_bar.setVisible(False)

  def go_to_dashboard(self):
    dashboard = DashboardPage(self.widget)
    self.widget.addWidget(dashboard)
    self.widget.setCurrentIndex(self.widget.currentIndex()+1)
