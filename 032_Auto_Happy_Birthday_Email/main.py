import smtplib
import pandas as pd
import datetime as dt
from random import randint

# Get email credentials
with open("secrets.txt", "r") as p:
    email = p.readline()
    passcode = p.readline()

# Randomly select message to send
with open(f"letter_templates/letter_{randint(1, 4)}.txt") as letter:
    letter = letter.read()

today = dt.datetime.now()
data = pd.read_csv("birthdays.csv")
birthdays = data.to_dict(orient="records")

for person in birthdays:
    if today.month == person["month"] and today.day == person["day"]:
        message = letter.replace("[NAME]", person["name"])
        with smtplib.SMTP("smtp.gmail.com", port=587) as server:
            server.starttls()
            server.login(user=email, password=passcode)
            server.sendmail(
                from_addr=email,
                to_addrs=person["email"],
                msg=f"Subject:Happy Birthday!\n\n{message}"
            )
