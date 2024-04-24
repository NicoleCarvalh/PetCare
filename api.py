import os
import requests
from dotenv import load_dotenv

load_dotenv()

def verify_credentials(email, password):
  api_key = os.getenv("API_KEY")

  if not api_key:
    raise ValueError("API_KEY não encontrada no arquivo .env")
  
  url = f"https://api-petcare.onrender.com/employees?auth={api_key}"
  payload = {"email": email, "password": password}
  response = requests.get(url, json=payload)

  if 'error' in response.json(): 
    # Return data 
    return False
  else:
    # Raise exception if there's an error
    return True


# # Example of use
# if __name__ == "__main__":
#   email = "arthur@gmail.com"
#   password = "123"

#   try:
#     data = verify_credentials(email, password)
#     print("Dados do usuário:", data)
#   except Exception as e:
#     print("Erro ao verificar credenciais:", e)

# if response.status_code == 200:
#   # Return data 
#   return response.json()
# else:
#   # Raise exception if there's an error
#   response.raise_for_status()