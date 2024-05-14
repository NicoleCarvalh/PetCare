from datetime import datetime
import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")
if not api_key:
  raise ValueError("API_KEY não encontrada no arquivo .env")

# API Endpoints
employees_url = f"https://api-petcare.onrender.com/employees?auth={api_key}"
sales_url = f"https://api-petcare.onrender.com/sales?auth={api_key}"
clients_url = f"https://api-petcare.onrender.com/clients?auth={api_key}"
products_url = f"https://api-petcare.onrender.com/products?auth={api_key}"


def verify_credentials(email, password):
  payload = {"email": email, "password": password}
  response = requests.get(employees_url, json=payload)

  if response.status_code == 200: 
    return True
  else:
    return False


def get_employees_list():
  try:
    response = requests.get(employees_url)
    data = response.json()

    if response.status_code == 200: 
      return data
    else:
      print("Erro ao acessar a API: ", response.status_code)

  except Exception as e:
    print("Erro ao acessar API: ", str(e))


def get_sales_list():
  try:
    response = requests.get(sales_url)
    data = response.json()

    if response.status_code == 200:
      # print(data)
      return data
    else: 
      print("Erro ao acessar a API: ", response.status_code)
  
  except Exception as e:
    print("Erro ao acessar API: ", str(e))


def get_client_name(client_id):
  try:
    response = requests.get(clients_url)
    data = response.json()

    if response.status_code == 200:
      for client in data:
        if client['id'] == client_id:
          return client['name']
      
      print("Cliente não encontrado.")
  
  except Exception as e:
    print("Erro ao acessar API de clientes: ", str(e))
    return None


#TODO arrumar listagem de produtos

def get_product_id_info(product_id):
  try:
    response = requests.get(f"https://api-petcare.onrender.com/products/{product_id}?auth={api_key}")

    if response.status_code == 200:
      return response.json()
    else: 
      print(f"Erro ao obter detalhes do produto {product_id}: ", response.status_code)
  
  except Exception as e:
    print(f"Erro ao obter detalhes do produto {product_id}: ", str(e))


###### UTILS - FORMATAÇÃO ###########

def format_date(date_str):
  date = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S+00:00")
  return date.strftime("%d/%m/%Y %H:%M:%S")


def format_value(value):
  formatted_value = "{:,.2f}".format(value).replace(",", "#").replace(".", ",").replace("#", ".")
  return f"R${formatted_value}"

