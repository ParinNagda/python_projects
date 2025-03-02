import requests
import datetime as dt

MY_LAT = 19.2304168
MY_LON = 73.0766709

parameters = {
    "lat": MY_LAT,
    "lng": MY_LON,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
sunrise = data['results']['sunrise'].split("T")[1].split(':')[0]
sunset = data['results']['sunset'].split("T")[1].split(':')[0]

print(sunrise)
print(sunset)