import requests
from datetime import datetime

from requests.api import head


pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

GRAPH_ID = "graph1"

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN	": TOKEN
}

# response = requests.post(
#     url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"


today = datetime.now()

# create a pixel
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "4.58",
}

# response = requests.post(url=pixel_creation_endpoint,
#                          json=pixel_data, headers=headers)
# print(response.text)


# update a pixel
whichday = today.strftime("%Y%m%d")

pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{whichday}"

new_pixel_data = {
    "quantity": "15.23"
}

# response = requests.put(url=pixel_update_endpoint,
#                         json=new_pixel_data, headers=headers)
# print(response.text)

# delete a pixel
pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{whichday}"

response = requests.delete(url=pixel_delete_endpoint, headers=headers)
print(response.text)
