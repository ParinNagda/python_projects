import os

import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
GENDER = "Male"
WEIGHT_KG = "69"
HEIGHT_CM = "145"
AGE = 27

APP_ID = os.environ.get('APP_ID')
API_KEY = os.environ.get('API_KEY')

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint =  "https://api.sheety.co/399ed006d2f2c25f9ec103947b96fbd5/workoutsSheet/workouts"
SHEETY_TOKEN = os.environ.get('SHEETY_TOKEN')

while 1:
    exercise_text = input("Tell me which exercises you did: ")

    headers = {
        "x-app-id": APP_ID,
        "x-app-key": API_KEY,
    }

    parameters = {
        "query": exercise_text,
        "gender": GENDER,
        "weight_kg": WEIGHT_KG,
        "height_cm": HEIGHT_CM,
        "age": AGE
    }
    try:
        response = requests.post(exercise_endpoint, json=parameters, headers=headers)
        result = response.json()
    except Exception as err:
        print(f"An exception occured to run AI {err}")
    today_date = datetime.now().strftime("%d/%m/%Y")
    now_time = datetime.now().strftime("%X")
    sheet_inputs = {}
    for exercise in result["exercises"]:
        sheet_inputs = {
            "workout": {
                "date": today_date,
                "time": now_time,
                "exercise": exercise["name"].title(),
                "duration": exercise["duration_min"],
                "calories": exercise["nf_calories"]
            }
        }


    bearer_headers = {
    "Authorization": f"Bearer {SHEETY_TOKEN}"
    }
    try:
        if sheet_inputs:
                sheet_response = requests.post(
                sheet_endpoint,
                json=sheet_inputs,
                headers=bearer_headers
        )
        get_sheet = requests.get(sheet_endpoint, headers=bearer_headers)
        get_sheet.raise_for_status()
        get_sheet_response = get_sheet.json()['workouts']

    except Exception as err:
        print(f"An exception has occured ${err}")


