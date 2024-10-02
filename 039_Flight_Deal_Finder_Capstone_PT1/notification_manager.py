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

    def send_alert(self, body):
        client = Client(self.sid, self.auth)
        message = client.messages.create(
            body=body,
            from_=self.twilio_num,
            to=self.my_num
        )
        print(message.status)
