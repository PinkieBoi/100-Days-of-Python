import os
import smtplib
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.sid = os.environ['TWILIO_SID']
        self.auth = os.environ['TWILIO_AUTH_TOKEN']
        self.twilio_num = os.environ['TWILIO_NUMBER']
        self.my_num = os.environ['TWILIO_VERIFIED_NUMBER']
        self.email = os.environ['GOOGLE_EMAIL']
        self.google_pw = os.environ['GOOGLE_APP_PASSWORD']

    def send_sms_alert(self, deal, destination, stopovers):
        price = deal['price']['grandTotal']
        home_airport = deal['itineraries'][0]['segments'][0]['departure']['iataCode']
        departure_date = deal['itineraries'][0]['segments'][0]['departure']['at'].split("T")[0]
        return_home = deal['itineraries'][1]['segments'][0]['departure']['at'].split("T")[0]
        if len(return_home) == 10:
            body = (f"Low price alert! £{price} from {home_airport} to {destination} "
                    f"on {departure_date} until {return_home} ({stopovers} layovers)")
        else:
            body = (f"Low price alert! £{price} from {home_airport} to {destination} "
                    f"on {departure_date} ({stopovers} layovers)")
        client = Client(self.sid, self.auth)
        message = client.messages.create(
            body=body,
            from_=self.twilio_num,
            to=self.my_num
        )
        print(message.status)

    def send_email_alert(self, deal, destination, stopovers, subscriber):
        body = ""
        with smtplib.SMTP("smtp.gmail.com", port=587) as server:
            server.starttls()
            server.login(self.email, self.google_pw)
            server.sendmail(
                from_addr=self.email,
                to_addrs=user_email,
                msg=body
            )
        pass
