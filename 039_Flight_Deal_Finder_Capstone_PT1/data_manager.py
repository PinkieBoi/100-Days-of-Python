import json
import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.endpoint = "https://api.sheety.co/aac89cb2101971d1bbd6f53efd56ab0d/flightDeals/prices"

        with open(file="env/secrets.json") as secrets:
            data = json.load(secrets)
            self.token = data["sheety_token"]
        self.header = {"authentication": self.token}

    def get_sheet(self):
        response = requests.get(
            url=self.endpoint,
            headers=self.header
        )
        return response.json()

    def edit_sheet(self, edit, row):
        response = requests.put(
            url=f"{self.endpoint}/{row}",
            headers=self.header,
            json={
                'price': {
                    'lowestPrice': edit
                }
            }
        )
        return response.text
