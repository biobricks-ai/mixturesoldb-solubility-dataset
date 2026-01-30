import requests
import json

def search_dataset():
    query = "MixtureSolDB"
    url = "https://zenodo.org/api/records"
    params = {'q': query, 'size': 1}
    response = requests.get(url, params=params)
    data = response.json()
    
    hits = data.get('hits', {}).get('hits', [])
    if hits:
        hit = hits[0]
        print(f"License: {hit['metadata'].get('license')}")

if __name__ == "__main__":
    search_dataset()
