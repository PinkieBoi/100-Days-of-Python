import os
import requests
import datetime as dt
from dotenv import load_dotenv

load_dotenv()


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.endpoint = "https://test.api.amadeus.com/v"
        self.api_key = os.environ['AMADEUS_API_KEY']
        self.api_secret = os.environ['AMADEUS_SECRET']
        self.token = ""

    def get_oauth_token(self):
        version = 1
        response = requests.post(
            url=f"{self.endpoint}{version}/security/oauth2/token",
            headers={
                "Content-Type": "application/x-www-form-urlencoded",
            },
            data={
                "grant_type": "client_credentials",
                "client_id": self.api_key,
                "client_secret": self.api_secret
            }
        ).json()
        self.token = f"{response['token_type']} {response['access_token']}"

    def get_city_data(self, city):
        version = 1
        res = requests.get(
            url=f"{self.endpoint}{version}/reference-data/locations/cities",
            headers={
                "Authorization": self.token
            },
            params={
                "keyword": city,
                "max": 1,
                "include": "AIRPORTS"
            }
        ).json()
        return res['data'][0]['iataCode']
    
    def get_flight_offers(self, city_code, price, days_to_depart, duration, direct_only="true"):
        days = days_to_depart
        version = 2
        res = requests.get(
            url=f"{self.endpoint}{version}/shopping/flight-offers",
            headers={
                "Authorization": self.token
            },
            params={
                "originLocationCode": "LON",
                "destinationLocationCode": city_code,
                "departureDate": dt.datetime.strftime(dt.date.today() + dt.timedelta(days=days), "%Y-%m-%d"),
                "returnDate": dt.datetime.strftime(dt.date.today() + dt.timedelta(days=(days + duration)), "%Y-%m-%d"),
                "adults": 1,
                "currencyCode": "GBP",
                "nonStop": direct_only,
                "maxPrice": round(float(price))
            }
        )
        return res.json()
