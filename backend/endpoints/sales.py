import requests
from backend.routes import sales_url

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
