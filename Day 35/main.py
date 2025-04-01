import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()


account_sid = os.environ.get('TWILIO_ACCOUNT')
auth_token = os.environ.get('TWILIO_TOKEN')
api_key = os.environ.get('WEATHER_KEY')

parameters = {
    "lat": 46.947975,
    "lon": 7.447447,
    "appid":api_key,
    "cnt":4
}


api_url = "https://api.openweathermap.org/data/2.5/forecast"

response = requests.get(api_url, params=parameters)

response.raise_for_status()

weather_data = response.json()

will_it_rain = False;
for hour_data in weather_data["list"]:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < 900:
        will_it_rain = True

if will_it_rain:
    client = Client(account_sid, auth_token)
    try:
        message = client.messages.create(
            from_='+18103446383',
            body='Please carry your umbrella',
            to='+917977525271'
        )
        print(f"Message sent: {message.sid}")
    except Exception as e:
        print(f"Failed to send message: {e}")




