import requests


APIKEY = "YOUR_API_KEY_HERE"

def get_place_reviews(place_id):
    url = f"https://cent.ischool-iot.net/api/google_places/details?place_id={place_id}&key={APIKEY}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def analyze_sentiment(text):
    url = f"https://cent.ischool-iot.net/api/azure/sentiment?key={APIKEY}"
    response = requests.post(url, json={"text": text})
    response.raise_for_status()
    return response.json()

def extract_entities(text):
    url = f"https://cent.ischool-iot.net/api/azure/entities?key={APIKEY}"
    response = requests.post(url, json={"text": text})
    response.raise_for_status()
    return response.json()
