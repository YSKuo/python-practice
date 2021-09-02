import os
import requests
from datetime import date, datetime
from dotenv import load_dotenv

load_dotenv()

GENDER = "male"
WEIGHT_KG = 65
HEIGHT_CM = 170
AGE = 31

NUTRITIONIX_APP_ID = os.getenv('NUTRITIONIX_APP_ID')
NUTRITIONIX_API_KEY = os.getenv('NUTRITIONIX_API_KEY')
SHEETY_BEARER_AUTH = os.getenv('SHEETY_BEARER_AUTH')

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = os.getenv('sheety_endpoint')

nutritionix_headers = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
    "Content-Type": "application/json"
}

exercise_text = input("Tell me which exercises you did: ")

nutritionix_body = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

sheety_headers = {
    "Authorization": SHEETY_BEARER_AUTH
}

nutritionix_response = requests.post(url=nutritionix_endpoint,
                                     headers=nutritionix_headers, json=nutritionix_body)
exercise_data = nutritionix_response.json()['exercises']

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for data in exercise_data:
    sheety_body = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": data["user_input"].title(),
            "duration": data["duration_min"],
            "calories": data["nf_calories"],
        }
    }
    sheety_response = requests.post(
        url=sheety_endpoint, headers=sheety_headers, json=sheety_body)
    print(sheety_response.text)
