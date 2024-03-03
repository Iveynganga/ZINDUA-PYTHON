import requests
from bs4 import BeautifulSoup

url = "https://www.jumia.co.ke/flash-sales/"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

#finding the item name
item_names = soup.find_all('div', class_="name")

for item_name in item_names:
    print(item_name.text)

#finding the item price
item_prices = soup.find_all('div', class_="prc" )

for item_price in item_prices:
    print(item_price.text)

#finding the number of items

