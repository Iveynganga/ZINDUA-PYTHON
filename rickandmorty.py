import requests
import csv

#fetching the number of characters
def fetch_characters():
    url = "https://rickandmortyapi.com/api/character/"

    characters = [20]
    response = requests.get(url)

    print(characters)

#fetching the number of locations
def fetch_locations():
    url = "https://rickandmortyapi.com/api/location/"
    

    locations = [20]
    response = requests.get(url)

    print(locations)

#fetching the number of episodes
def fetch_episodes():
    url = "https://rickandmortyapi.com/api/episode/"
    
    response = requests.get(url)

    episodes = [20]
    response = requests.get(url)

    print(episodes)
