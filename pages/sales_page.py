from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QPushButton, QMessageBox
from api.api import get_sales_list, get_client_name, format_date, format_value, get_product_id_info

def populate_table(self):
  sales_data = get_sales_list()

  row_count = len(sales_data)

  self.sales_table.setRowCount(row_count)

  for row, sale in enumerate(sales_data):
  
    self.sales_table.setItem(row, 0, QTableWidgetItem(str(sale['id'])))
    client_name = get_client_name(sale['client_id'])
    self.sales_table.setItem(row, 1, QTableWidgetItem(client_name if client_name else "Cliente Desconhecido"))
    self.sales_table.setItem(row, 2, QTableWidgetItem(format_date(sale['date_time'])))
    self.sales_table.setItem(row, 3, QTableWidgetItem(format_value(sale['total'])))
    self.sales_table.setItem(row, 4, QTableWidgetItem(str(sale['payment_method'])))
    self.sales_table.setItem(row, 5, QTableWidgetItem(str(sale['products'])))

  
    btn_view_items = QPushButton("Ver Itens")
    btn_view_items.clicked.connect(lambda _, row=row: self.view_items(row))
    self.sales_table.setCellWidget(row, 5, btn_view_items)  


def view_items(self, row):
  # Recupera o ID da venda da linha clicada
  sale_id = int(self.sales_table.item(row, 0).text())

  sale = get_sales_list()[row]

  items_details = []

  for item in sale['products']:
    product_id = item['product_id']
    
    quantity = item['quantity']

    product_details = get_product_id_info(product_id)

    if product_details:
        product_name = product_details['name']

        unit_price = product_details['price']
        
        total_price_item = quantity * unit_price
        
        items_details.append(f"{product_name} - {quantity} unidades - R${total_price_item:.2f}")
    else:
        items_details.append(f"Produto não encontrado - ID: {product_id}")

# Cria uma mensagem com os detalhes dos itens da venda
  items_text = "\n".join(items_details)

  # Cria a janela de diálogo para mostrar os detalhes dos itens da venda
  items_dialog = QMessageBox()
  items_dialog.setWindowTitle("Itens da Venda")
  items_dialog.setText(f"Itens da Venda {sale_id}:\n{items_text}")
  items_dialog.exec_()

