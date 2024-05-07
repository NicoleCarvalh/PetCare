from PyQt5.QtWidgets import QApplication, QDialog, QTableWidgetItem, QPushButton, QVBoxLayout, QMessageBox
from PyQt5.uic import loadUi
import sys

class SalesWindow(QDialog):
  def __init__(self):
    super().__init__()
    loadUi("layouts/sales.ui", self)

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
      self.tableWidget.insertRow(row)
      self.tableWidget.setItem(row, 0, QTableWidgetItem(str(sale_id)))
      self.tableWidget.setItem(row, 1, QTableWidgetItem(client))
      self.tableWidget.setItem(row, 2, QTableWidgetItem(str(total)))

      # Adiciona o botão para visualizar os itens da venda
      btn_view_items = QPushButton("Ver Itens")
      btn_view_items.clicked.connect(lambda state, row=row: self.view_items(row))
      self.tableWidget.setCellWidget(row, 3, btn_view_items)

  def view_items(self, row):
    # Recupera o ID da venda da linha clicada
    sale_id = int(self.tableWidget.item(row, 0).text())

    # Aqui você abriria uma janela pop-up para mostrar os itens da venda
    # Como exemplo, usaremos uma caixa de diálogo simples do QMessageBox
    items_dialog = QMessageBox()
    items_dialog.setWindowTitle("Itens da Venda")
    items_dialog.setText(f"Itens da Venda {sale_id}:\n"
                          "Produto 1 - R$10\n"
                          "Produto 2 - R$20\n"
                          "Produto 3 - R$15")
    items_dialog.exec_()

if __name__ == "__main__":
  app = QApplication(sys.argv)
  sales_window = SalesWindow()
  sales_window.show()
  sys.exit(app.exec_())
