import requests
from backend.routes import clients_url

def get_clients_list():
  try:
    response = requests.get(clients_url)
    data = response.json()

    if response.status_code == 200:
      return data
    else:
      print("Erro ao acessar a API: ", response.status_code)

  except Exception as e:
    print("Erro ao acessar API: ", str(e))
