import time

import requests
import datetime as dt

MY_LAT = 19.2304168
MY_LON = 73.0766709

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()
    iss_longitude = data["iss_position"]["longitude"]
    iss_latitude = data["iss_position"]["latitude"]

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LON-5 <= iss_longitude <= MY_LON+5:
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LON,
        "formatted": 0
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()

    data = response.json()
    sunrise = int(data['results']['sunrise'].split("T")[1].split(':')[0])
    sunset = int(data['results']['sunset'].split("T")[1].split(':')[0])
    time_now = dt.datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True

while True:
    if is_iss_overhead() and is_night():
        print("ISS is above my head")