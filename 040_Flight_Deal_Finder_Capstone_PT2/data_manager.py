import os
import requests
from dotenv import load_dotenv

load_dotenv()


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.endpoint = "https://api.sheety.co/aac89cb2101971d1bbd6f53efd56ab0d/flightDeals/"
        self.token = os.environ['SHEETY_TOKEN']
        self.header = {"Authentication": f"Bearer {self.token}"}

    def get_sheet(self, sheet_name):
        response = requests.get(
            url=f"{self.endpoint}{sheet_name}",
            headers=self.header
        )
        return response.json()

    def edit_sheet(self, edit, data, row):
        response = requests.put(
            url=f"{self.endpoint}/{row}",
            headers=self.header,
            json={
                'price': {
                    edit: data
                }
            }
        )
        return response.text
