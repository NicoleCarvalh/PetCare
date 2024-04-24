import os
import requests
from dotenv import load_dotenv
from requests_toolbelt.multipart.encoder import MultipartEncoder
import uuid

load_dotenv()

def register_employee(name, email, password):
  api_key = os.getenv("API_KEY")

  if not api_key:
    raise ValueError("API_KEY não encontrada no arquivo .env")
  
  url = f"https://api-petcare.onrender.com/employees?auth={api_key}"

  payload = MultipartEncoder(
    fields={
        'name': name,
        'email': email,
        'password': password
    }
  )

  headers = {'Content-Type': payload.content_type}

  # response = requests.post(url, data=payload, headers=headers)
  try:
    response = requests.post(url, data=payload, headers=headers)
    response.raise_for_status()  # Raise exception for 4xx or 5xx status codes

    if response.status_code == 200:
      return response.json()
    else:
      return None  # Returning None if unexpected status code
    
  except requests.exceptions.RequestException as e:
    print("Erro na requisição:", e)
    return None  # Returning None in case of any exception


# Example of use
if __name__ == "__main__":
  name = "ClaudioT"
  email = "teste2@teste.com"
  password = "123"

  try:
    data = register_employee(name, email, password)
    print("Dados do usuário:", data)
  except Exception as e:
    print("Erro ao inserir credenciais:", e)


############## FUNÇÃO FEITA PELO GEMINI QUE ADICIONAVA \N AO FIM DOS PARÂMETROS
# def generate_multipart_data(payload):
  #   boundary = str(uuid.uuid4())

  #   parts = []
  #   for key, value in payload.items():
  #     part = f'--{boundary}\nContent-Disposition: form-data; name="{key}"\n\n{value}\n'
  #     parts.append(part)

  #   body = '\n'.join(parts) + f'\n--{boundary}--\n'
  #   return body, boundary