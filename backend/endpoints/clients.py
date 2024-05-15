import requests
from backend.routes import clients_url

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