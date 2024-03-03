import requests
from bs4 import BeautifulSoup
import csv

url = ("https://www.nytimes.com/")

response = requests.get(url)

#print('results.status_code')

soup = BeautifulSoup(response.content, "html.parser")

articles = soup.find_all('p', class_="indicate-hover")[:10]
data = []

print(articles)

#finding the top 10 articles
#for article in articles:
    #title = article.find('h2').text.strip()
    #description = article.find('p').text.strip()
    #data.append({'title': title, 'description': description})

#print (data)

with open('nytimes.csv', 'w') as file:
    writer = csv.DictWriter(file, fieldnames =['title', 'description'])
    writer.writeheader()
    writer.writerows(data)