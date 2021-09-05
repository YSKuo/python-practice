import os
import requests
from dotenv import load_dotenv

load_dotenv()

sheety_auth = os.getenv("SHEETY_AUTH_FOR_FLIGHT")


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.header = {
            "Authorization": sheety_auth
        }
        self.sheet_data = None
        self.end_point = "https://api.sheety.co/95cca73806f2cb1d9d53a9336437fb49/flightDeals/prices"

    def get_sheet_data(self):
        response = requests.get(
            url=self.end_point, headers=self.header)
        self.sheet_data = response.json()["prices"]

    def update_row(self, id, data):
        url = f"{self.end_point}/{id}"
        body = {
            "price": {
                "city": data["city"],
                "iataCode": data["iataCode"],
                "lowestPrice": data["lowestPrice"],
            }
        }
        response = requests.put(url=url, headers=self.header, json=body)
