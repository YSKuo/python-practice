import requests
from datetime import datetime


# END_POINT = "http://api.open-notify.org/iss-now.json"

# response = requests.get(url=END_POINT)
# response.raise_for_status()

# data = response.json()

# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]

# iss_position = (longitude, latitude)
# print(iss_position)


END_POINT = "https://api.sunrise-sunset.org/json"
MY_LAT = 25.032969
MY_LONG = 121.565414

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get(url=END_POINT, params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

time_now = datetime.now()

print(data)