import json
import requests
import datetime as dt


def add_pixel(n):
    date = dt.date.today().strftime("%Y%m%d")
    post_url = f"{GRAPH_EP}/{graph_config['id']}"
    response = requests.post(
        url=post_url,
        headers=header,
        json={
            "date": date,
            "quantity": str(n)
        }
    )
    print(response.text)


def update_pixel(n):
    date = str(dt.date.today().strftime("%Y%m%d"))
    post_url = f"{GRAPH_EP}/{graph_config['id']}/{date}"
    initial_value = requests.get(
        url=post_url,
        headers=header
    )
    response = requests.put(
        url=post_url,
        headers=header,
        json={
            "quantity": str(int(initial_value.json()["quantity"]) + n)
        }
    )
    print(response.text)


with open(file="env/secrets.json") as secrets:
    data = json.load(secrets)
    USERNAME = data["username"]
    TOKEN = data["token"]

PIXELA_URL = "https://pixe.la/v1/users"
GRAPH_EP = f"{PIXELA_URL}/{USERNAME}/graphs"

header = {
    "X-USER-TOKEN": TOKEN
}

graph_config = {
    "id": "pythonproject",
    "name": "100 Days of Python",
    "unit": "commit",
    "type": "int",
    "color": "ajisai"
}

# graph_creation = requests.post(url=GRAPH_EP, headers=header, json=graph_config)
# post_pixel(1)
update_pixel(2)
