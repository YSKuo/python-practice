import os
import requests
from flight_data import FlightData
from dotenv import load_dotenv

load_dotenv()


TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
tequila_api_key = os.getenv("TEQUILA_API_KEY")


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):

    def get_iata_code(self, city):
        api_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": tequila_api_key}
        parameters = {
            "term": city,
            "location_types": "airport",
            "active_only": "true"
        }
        response = requests.get(
            url=api_endpoint, headers=headers, params=parameters)
        location_data = response.json()["locations"]
        return location_data[0]["city"]["code"]

    def get_flight_data(self, origin_city_code, destination_city_code, from_time, to_time):
        api_endpoint = f"{TEQUILA_ENDPOINT}/v2/search"
        headers = {"apikey": tequila_api_key}
        parameters = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP",
        }

        response = requests.get(
            url=api_endpoint, headers=headers, params=parameters)

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            depart_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0])
        print(f"{destination_city_code}: £{flight_data.price}")
        return flight_data
