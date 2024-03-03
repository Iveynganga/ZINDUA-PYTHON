#scrape https://hojaleaks.com/python and get the titles/headings of the first three articles
import requests
from bs4 import BeautifulSoup

url = "https://hojaleaks.com/python"

response = requests.get(url)

#print(response.status_code)

#print(response)

soup = BeautifulSoup(response.content, "html.parser")

#print(soup)

articles = soup.find_all('h1')

for article in articles:
    print(article.text)