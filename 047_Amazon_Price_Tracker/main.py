import os
import smtplib
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()
FROM_MAIL = os.environ['GOOGLE_EMAIL_ADDR']
TO_MAIL = os.environ['MY_EMAIL']
SERVER_PASSWD = os.environ['GOOGLE_APP_PASS']

static_url = "https://appbrewery.github.io/instant_pot"
with open("info.txt") as file:
    item_url = file.readline()

headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0",
           "Accept-Language": "en-US,en;q=0.5"}

response = requests.get(url=item_url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
current_price = float(soup.find(class_="a-price-whole").text + soup.find(class_="a-price-fraction").text)
max_price = 170

item_name = soup.title.getText().split(":")[0]
alert_message = f"The {item_name} you are watching on Amazon is now available for £{current_price} \nLink: {item_url}"

if current_price <= max_price:
    with smtplib.SMTP("smtp.gmail.com", port=587) as server:
        server.starttls()
        server.login(user=FROM_MAIL, password=SERVER_PASSWD)
        eggs = server.sendmail(
            from_addr=FROM_MAIL,
            to_addrs=TO_MAIL,
            msg=f"Subject:Amazon Price Alert\n\n{alert_message}".encode("utf-8")
        )
