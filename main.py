from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot, QFile, QTextStream, QUrl, Qt
from PyQt5.QtGui import QIcon, QFont, QFontDatabase, QDesktopServices
from PyQt5 import uic, QtWidgets
from api import verify_credentials
import sys

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

    self.full_menu.hide()
    self.dashboard_btn_2.setChecked(True)
    self.exit_btn_1.clicked.connect(self.exit_to_login)
    self.exit_btn_2.clicked.connect(self.exit_to_login)

  def exit_to_login(self):
    widget.setCurrentIndex(0)

  # Function for searching
  def search(self):
    self.stackedWidget.setCurrentIndex(5)
    search_text = self.search_input.text().strip()
    if search_text:
      self.label_6.setText(search_text)
  


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

    #####################################
    # Populando a tabela com dados fictícios para teste
    self.populate_table()

  def populate_table(self):
    # Dados fictícios de vendas (id, cliente, total)
    sales_data = [
      (1, "Cliente 1", 100),
      (2, "Cliente 2", 150),
      (3, "Cliente 3", 200)
    ]

    # Loop para adicionar cada venda à tabela
    for row, (sale_id, client, total) in enumerate(sales_data):
      # Adiciona os dados da venda à tabela
      self.sales_table.insertRow(row)
      self.sales_table.setItem(row, 0, QTableWidgetItem(str(sale_id)))
      self.sales_table.setItem(row, 1, QTableWidgetItem(client))
      self.sales_table.setItem(row, 2, QTableWidgetItem(str(total)))

      # Criando o botão "Ver Itens"
      btn_view_items = QPushButton("Ver Itens")
      btn_view_items.setStyleSheet(
        "QPushButton {"
        "   background-color: #389bf2;"
        "   border-radius: 15px;"
        "   color: white;"
        "   padding: 5px 5px;"
        "   font-size: 12px;"
        "   font-weight: bold;"
        "   max-width: 80px;"
        "   max-height: 20px;"
        "}"
        "QPushButton::hover {"
        "   background-color: #FFBC00;"
        "}"    
      )

      btn_view_items.clicked.connect(self.view_items)
      self.sales_table.setCellWidget(row, 3, btn_view_items)

  def view_items(self, row):
    # Recupera o ID da venda da linha clicada
    sale_id = int(self.sales_table.item(row, 0).text())

    # Aqui você abriria uma janela pop-up para mostrar os itens da venda
    # Como exemplo, usaremos uma caixa de diálogo simples do QMessageBox
    items_dialog = QMessageBox()
    items_dialog.setWindowTitle("Itens da Venda")
    items_dialog.setText(f"Itens da Venda {sale_id}:\n"
                          "Produto 1 - R$10\n"
                          "Produto 2 - R$20\n"
                          "Produto 3 - R$15")
    items_dialog.exec_()
  
  #####################################################

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