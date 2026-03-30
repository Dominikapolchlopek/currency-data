import requests
import json
import os

API_KEY = os.getenv('FIXER_API_KEY')
URL = f"http://data.fixer.io/api/latest?access_key={API_KEY}"

def fetch_data():
    try:
        response = requests.get(URL)
        data = response.json()
        
        if data.get('success'):
            # Zapis do pliku rates.json
            with open('rates.json', 'w') as f:
                json.dump(data, f, indent=4)
            print("Success.")
        else:
            print(f"API error: {data.get('error')}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    fetch_data()
