import json
import requests
import datetime as dt


def log_exercise():
    log_response = requests.post(
        url=SHEETY_EP,
        headers=sheety_header,
        json={
            "workout": {
                "date": str(dt.date.today().strftime("%d/%m/%Y")),
                "time": timestamp,
                "exercise": exercise.title(),
                "duration": int(duration),
                "calories": nix_response.json()['exercises'][0]["nf_calories"],
            }
        }
    )
    print(log_response)


with open(file="env/secrets.json") as secrets:
    data = json.load(secrets)
    NIX_ID = data["nutrition_id"]
    NIX_API_KEY = data["nutrition_api_key"]
    SHEETY_TOKEN = data["sheety_token"]

NIX_headers = {
    'Content-Type': 'application/json',
    'x-app-id': NIX_ID,
    'x-app-key': NIX_API_KEY
}

sheety_header = {
    "Authorization": SHEETY_TOKEN
}

NL_EXERCISE_EP = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_EP = "https://api.sheety.co/aac89cb2101971d1bbd6f53efd56ab0d/myWorkouts/workouts"

exercise = input("Exercise: ")
distance = input("Distance(km): ")
duration = input("Duration(mins): ")
timestamp = input("Time Completed(24hr): ")
# .split(":"))
# timestamp = dt.time(int(timestamp[0]), int(timestamp[1]))

if len(distance) > 0:
    body = f"{exercise} {distance}km over {duration} minutes"
else:
    body = f"{exercise} for {duration} minutes"

nix_response = requests.post(
    url=NL_EXERCISE_EP,
    headers=NIX_headers,
    json={
        "query": body
    }
)

log_exercise()
