import os
from os import environ

import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/399ed006d2f2c25f9ec103947b96fbd5/myFlightDeals/prices"
SHEETY_TOKEN = environ.get("SHEETY_TOKEN")

class DataManager:

    def __init__(self):
        self.bearer_headers = {
            "Authorization": f"Bearer {SHEETY_TOKEN}"
        }
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=self.bearer_headers)
        data = response.json()
        self.destination_data = data["prices"]
        print(data)
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=self.bearer_headers
            )
            print(response.text)