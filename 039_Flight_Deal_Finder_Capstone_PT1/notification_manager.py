import json
from twilio.rest import Client


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        with open(file="env/secrets.json") as secrets:
            data = json.load(secrets)
            self.sid = data['twilio_sid']
            self.auth = data['twilio_auth']
            self.twilio_num = data['twilio_number']
            self.my_num = data['my_number']

    def send_alert(self, deal):
        price = deal["price"]
        home_airport = deal["departureIataCode"]
        destination = deal["destinationIataCode"]
        departure_date = deal["departureDate"].split("T")[0]
        return_home = deal["returnDate"].split("T")[0]
        body = f"Low price alert! £{price} from {home_airport} to {destination} on {departure_date} until {return_home}"
        client = Client(self.sid, self.auth)
        message = client.messages.create(
            body=body,
            from_=self.twilio_num,
            to=self.my_num
        )
        print(message.status)
