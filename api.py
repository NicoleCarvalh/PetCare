import requests

def verify_credentials(email, password):
  url = "https://api-petcare.onrender.com/employees"
  payload = {"email": email, "password": password}
  response = requests.post(url, json=payload)
  return response
