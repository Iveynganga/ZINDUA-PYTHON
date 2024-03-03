import requests
import re
from bs4 import BeautifulSoup
import csv

url = ("https://jumia.co.ke/")

response = requests.get(url)

#print(response.status_code)

soup = BeautifulSoup(response.content, "html.parser")

#finding the product name
product_names = soup.find_all('div', class_="name")

for product_name in product_names:
    print(product_name.text)

#finding the price
    product_prices = soup.find_all('div', class_="prc")

for product_price in product_prices:
    print(product_price.text)

#finding the discount
    product_discounts = soup.find_all('div', class_="bdg _dsct")

for product_discount in product_discounts:
    print(product_discount.text)

#finding the product review
    product_reviews = soup.find_all('div', class_="stars _m -mvs")

for product_review in product_reviews:
    print(product_review.text)

#combining the data to a csv file
with open('jumia.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(product_names)