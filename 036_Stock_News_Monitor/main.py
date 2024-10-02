import json
import requests
import datetime as dt
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

with open(file="env/secrets.json") as secrets:
    data = json.load(secrets)
    TWILIO_SID = data["twilio_sid"]
    TWILIO_AUTH = data["twilio_auth"]
    TWILIO_NUM = data["twilio_number"]
    MY_NUMBER = data["my_number"]
    NEWSAPI_KEY = data["newsapi_key"]
    ALPHAVANTAGE = data["alphavantage"]

alph_url = "https://www.alphavantage.co/query"
alph_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": ALPHAVANTAGE
}
stock_data = requests.get(url=alph_url, params=alph_params).json()
data = stock_data["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
y_close = float(yesterday_data["4. close"])
dby_data = data_list[1]
dby_close = float(dby_data["4. close"])
pc_change = (abs(y_close - dby_close) / y_close) * 100

if pc_change > 1:
    newsapi_url = "https://newsapi.org/v2/everything"
    newsapi_params = {
        "q": COMPANY_NAME,
        "from": dt.date.today() - dt.timedelta(days=1),
        "to": dt.date.today(),
        "sortBy": "popular",
        "apikey": NEWSAPI_KEY,
        "pageSize": 3,
        "page": 1
    }

    if y_close < dby_close:
        sign = "🔻"
    else:
        sign = "🔺"

    stock_change = f"{STOCK} {sign}{round(pc_change, 3)}%"

    news_data = requests.get(url=newsapi_url, params=newsapi_params).json()
    news_item1 = ["...".join([news_data["articles"][0]["title"][:50], news_data["articles"][0]["url"]])]
    news_item2 = ["...".join([news_data["articles"][1]["title"][:50], news_data["articles"][1]["url"]])]
    news_item3 = ["...".join([news_data["articles"][2]["title"][:50], news_data["articles"][2]["url"]])]
    sms_alerts = [stock_change, news_item1, news_item2, news_item3]

    client = Client(TWILIO_SID, TWILIO_AUTH)
    for _ in sms_alerts:
        message = client.messages.create(
            body=_,
            from_=TWILIO_NUM,
            to=MY_NUMBER
        )
