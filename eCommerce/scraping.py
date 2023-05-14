import requests
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eCommerce.settings')
django.setup()
from bs4 import BeautifulSoup
from store.models import Product
from decimal import Decimal

url = 'https://www.jumia.ma/pc-portables/'
html = requests.get(url)
# print(html.text)

s = BeautifulSoup(html.content, 'html.parser')
results = s.find(id='jm')
product_name_tags = results.findAll('h3', class_='name')

product_names = []
for item in product_name_tags:
    product_names.append(item.text)

product_price_tags = results.findAll('div', class_='prc')
product_prices = []
for item in product_price_tags:
    item = item.text[:-4]
    item = item.replace(',', '')
    product_prices.append(Decimal(item))

products = [item for item in zip(product_names, product_prices)]
for item in products:
    model_instance = Product(name=item[0], price=item[1])
    model_instance.save()
print('succes!')



