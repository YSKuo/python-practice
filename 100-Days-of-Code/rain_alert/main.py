import requests
import os
from twilio.rest import Client
# from private_info import *

API_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"

API_KEY = os.environ.get('OWN_API_KEY')
auth_token = os.environ.get("AUTH_TOKEN")


# Taipei
# MY_LAT = 25.032969
# MY_LONG = 121.565414

# Brodnica
MY_LAT = 53.256771
MY_LONG = 19.403490

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

response = requests.get(url=API_ENDPOINT, params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data['weather'][0]['id']

    if int(condition_code) < 700:
        will_rain = True
        break


if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="Rain today. Remember to bring an ☔️",
            from_=FROM_NUMBER,
            to=TO_NUMBER
        )
    print(message.status)
