import requests
from api.api import employees_url


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
