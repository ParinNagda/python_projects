from traceback import print_tb
import  datetime as dt
import requests
import os

from aiohttp.helpers import TOKEN
from dotenv import load_dotenv

load_dotenv()

token = os.environ.get('TOKEN')
username = os.environ.get('USERNAME_PIXEL')
print(username)

pixela_endpoint = 'https://pixe.la/v1/users'
# user_params = {
#     'token': token,
#     'username':username,
#     'agreeTermsOfService': 'yes',
#     'notMinor': 'yes'
# }
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
graph_endpoint = f"{pixela_endpoint}/{username}/graphs"
graph_id = "graph12"
# graph_param = {
#     "id": graph_id,
#     "name": "Running",
#     "unit": "Km",
#     "type": "float",
#     "color": "ajisai",
# }
# headers = {
#     "X-USER-TOKEN": token
# }
# response = requests.post(url=graph_endpoint, json=graph_param, headers=headers)
# print(response.text)

post_pixel_endpoint = f"{graph_endpoint}/{graph_id}"
date = dt.date.today().strftime("%Y%m%d")
print(date)
post_pixel_param = {
    "date":date,
    "quantity":"25"
}
headers = {
    "X-USER-TOKEN": token
}

# pixel_response = requests.post(url=post_pixel_endpoint, json=post_pixel_param, headers=headers)
# print(pixel_response.text)

put_pixel_endpoint = f"{post_pixel_endpoint}/{date}"
print(put_pixel_endpoint)
put_pixel_param = {
    "quantity": "15"
}

pixel_response = requests.put(url=put_pixel_endpoint, json=put_pixel_param, headers=headers)
print(pixel_response)