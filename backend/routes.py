from datetime import datetime
import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")
if not api_key:
  raise ValueError("API_KEY não encontrada no arquivo .env")

# API Endpoints
employees_url = f"https://api-pet-care.vercel.app/employees?auth={api_key}"
sales_url = f"https://api-pet-care.vercel.app/sales?completed=true&auth={api_key}"
clients_url = f"https://api-pet-care.vercel.app/clients?auth={api_key}"
products_url = f"https://api-pet-care.vercel.app/products?auth={api_key}"


###### UTILS - FORMATAÇÃO ###########

def format_date(date_str):
  date = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S+00:00")
  return date.strftime("%d/%m/%Y %H:%M:%S")


def format_value(value):
  formatted_value = "{:,.2f}".format(value).replace(",", "#").replace(".", ",").replace("#", ".")
  return f"R${formatted_value}"

