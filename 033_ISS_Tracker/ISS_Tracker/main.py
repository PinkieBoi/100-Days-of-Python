import time
import smtplib
import requests
import datetime as dt


def is_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_position = response.json()["iss_position"]
    if -0.070340 > float(iss_position["longitude"]) < -0.303134:
        if abs(params["lat"]) < float(iss_position["latitude"] > abs(params["lat"]) + 1):
            return True


def is_night():
    nighttime = requests.get(url="https://api.sunrise-sunset.org/json?", params=params)
    sunset = nighttime.json()["results"]["sunset"].split("T")[1].split(":")[:2]
    current_time = [(dt.datetime.today().hour - 12), dt.datetime.today().minute]
    if current_time[0] > int(sunset[0]):
        return True
    elif current_time[0] == int(sunset[0]) and current_time[1] >= sunset[1]:
        return True


def send_alert():
    with smtplib.SMTP("smtp.gmail.com", port=587) as server:
        server.starttls()
        server.login(user=EMAIl, password=PASSCODE)
        server.sendmail(
            from_addr=EMAIl,
            to_addrs="",
            msg="Subject:ISS Overhead\n\nLook up, the ISS is passing overhead!"
        )


with open("secrets.txt") as s:
    EMAIl = s.readline()
    PASSCODE = s.readline()

params = {
    "lat": 50.827778,
    "lng": -0.152778,
    "formatted": 0
}

while is_overhead() and is_night():
    send_alert()
    time.sleep(60)
