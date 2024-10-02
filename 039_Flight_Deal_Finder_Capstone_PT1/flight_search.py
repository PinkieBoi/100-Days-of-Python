import json
import requests
import datetime as dt


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.endpoint = "https://test.api.amadeus.com/v"
        self.token = ""
        self.airports = ["LHR", "LGW"]

        with open(file="env/secrets.json") as secrets:
            data = json.load(secrets)
            self.api_key = data["amadeus_key"]
            self.api_secret = data["amadeus_secret"]

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
                "include": "Airports"
            }
        )
        return res.json()

    def get_flight_offers(self, city_code, price):
        offers = []
        for day in range(1, 5):
            for airport in self.airports:
                version = 2
                res = requests.get(
                    url=f"{self.endpoint}{version}/shopping/flight-offers",
                    headers={
                        "Authorization": self.token
                    },
                    params={
                        "originLocationCode": airport,
                        "destinationLocationCode": city_code,
                        "departureDate": dt.datetime.strftime(dt.date.today() + dt.timedelta(days=day), "%Y-%m-%d"),
                        "adults": 1,
                        "currencyCode": "GBP",
                        # "maxPrice": int(price)
                    }
                ).json()
                for deal in res['data']:
                    offer = {
                        "iataCode": city_code,
                        "lowestPrice": deal['price']['grandTotal']
                    }
                    offers.append(offer)
        best_offer = {}
        for offer in offers:
            if len(best_offer) == 0 or float(best_offer['lowestPrice']) > float(offer['lowestPrice']):
                best_offer = offer
        return best_offer
