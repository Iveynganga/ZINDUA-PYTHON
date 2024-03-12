import requests

# Fetching the number of characters
def fetch_characters():
    url = "https://rickandmortyapi.com/api/character/"
    response = requests.get(url)
    
    if response.status_code == 200:
        characters = response.json()["info"]["count"]
        print(f"Number of characters: {characters}")
    else:
        print(f"Failed to fetch characters. Status code: {response.status_code}")

# Fetching the number of locations
def fetch_locations():
    url = "https://rickandmortyapi.com/api/location/"
    response = requests.get(url)
    
    if response.status_code == 200:
        locations = response.json()["info"]["count"]
        print(f"Number of locations: {locations}")
    else:
        print(f"Failed to fetch locations. Status code: {response.status_code}")

# Fetching the number of episodes
def fetch_episodes():
    url = "https://rickandmortyapi.com/api/episode/"
    response = requests.get(url)
    
    if response.status_code == 200:
        episodes = response.json()["info"]["count"]
        print(f"Number of episodes: {episodes}")
    else:
        print(f"Failed to fetch episodes. Status code: {response.status_code}")

    