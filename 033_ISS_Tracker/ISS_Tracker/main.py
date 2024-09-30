import smtplib
import requests
import datetime as dt


def send_alert():
    if float(iss_position["longitude"]) == params["lat"] and float(iss_position["latitude"]) == params["lng"]:
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
    "lng": -0.152778
}

# Get ISS position
response = requests.get(url="http://api.open-notify.org/iss-now.json")
iss_position = response.json()["iss_position"]

if dt.datetime.today().hour > 12:
    # Get nighttime hours
    nighttime = requests.get(url="https://api.sunrise-sunset.org/json?", params=params)
    sunset = nighttime.json()["results"]["sunset"].split()[0]
    sunset = sunset.split(":")
    current_time = [(dt.datetime.today().hour - 12), dt.datetime.today().minute]

    if current_time[0] < int(sunset[0]):
        send_alert()
    elif current_time[0] == int(sunset[0]) and current_time[1] <= sunset[1]:
        send_alert()

