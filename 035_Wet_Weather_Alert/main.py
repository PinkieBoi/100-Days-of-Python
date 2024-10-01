import json
import requests
from twilio.rest import Client

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"

with open("env/secrets.json") as secrets:
    data = json.load(secrets)
    OWM_KEY = data["owm_api_key"]
    TWILIO_SID = data["twilio_sid"]
    TWILIO_AUTH = data["twilio_auth"]
    TWILIO_NUM = data["twilio_number"]
    MY_NUMBER = data["my_number"]

owm_params = {
    "lon": -0.1395,
    "lat": 50.8284,
    "appid": OWM_KEY,
    "cnt": 4
}

owm_data = requests.get(url=OWM_ENDPOINT, params=owm_params).json()

for item in owm_data["list"]:
    if 299 < item["weather"][0]["id"] < 600:
        client = Client(TWILIO_SID, TWILIO_AUTH)
        message = client.messages.create(
            body="It is raining today, bring an umbrella.",
            from_=TWILIO_NUM,
            to=MY_NUMBER
        )
