import requests
import os
import json

def download_data():
    # Found via search 'MixtureSolDB' on Zenodo
    record_id = "18234735" 
    url = f"https://zenodo.org/api/records/{record_id}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    
    files = data['files']
    download_dir = "download"
    os.makedirs(download_dir, exist_ok=True)
    
    for file_info in files:
        file_url = file_info['links']['self']
        filename = file_info['key']
        print(f"Downloading {filename} from {file_url}")
        
        file_path = os.path.join(download_dir, filename)
        
        with requests.get(file_url, stream=True) as r:
            r.raise_for_status()
            with open(file_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
                    
if __name__ == "__main__":
    download_data()
