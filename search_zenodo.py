import requests
import json

def search_dataset():
    query = "MixtureSolDB"
    url = "https://zenodo.org/api/records"
    params = {'q': query, 'size': 5}
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    
    hits = data.get('hits', {}).get('hits', [])
    if not hits:
        print("No hits found for MixtureSolDB")
        return

    for hit in hits:
        print(f"ID: {hit['id']}")
        print(f"Title: {hit['metadata']['title']}")
        print(f"Links: {hit['links']['self']}")
        print("-" * 20)

if __name__ == "__main__":
    search_dataset()
