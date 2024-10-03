import time
from flight_data import FlightData
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
flight_search.get_oauth_token()
notifications = NotificationManager()

price_data = data_manager.get_sheet("prices")
subscriber_data = data_manager.get_sheet("users")

# for city in price_data:
#     iatacode = flight_search.get_city_data(city['city'])
#     data_manager.edit_sheet(
#         edit="iataCode",
#         data=iatacode,
#         row=city['id']
#     )
#     time.sleep(2)
#
# timespan = 2 * 30
timespan = 5
deals_email = []

for day in range(1, timespan):
    for city in data_manager.get_sheet()["prices"]:
        options = flight_search.get_flight_offers(city['iataCode'], city['lowestPrice'], day, 7)
        if len(options['data']) > 0:
            best_deal = FlightData().find_cheapest_option(options)
            if float(city['lowestPrice']) > float(best_deal[0]['price']['grandTotal']):
                old_price = city['lowestPrice']
                data_manager.edit_sheet("lowestPrice", best_deal[0]['price']['grandTotal'],  city['id'])
                price_alert = f"""
                Flight to {city['city']} down form £{old_price} to £{best_deal[0]['price']['grandTotal']}
                """
                deals_email.append([city['city'], best_deal])
                notifications.send_sms_alert(deal=best_deal[0], destination=city['iataCode'], stopovers=best_deal[1])
        # if city['city'] in subscriber_data:
        time.sleep(2)

# for person in subscriber_data:
#     if city['city'] in person['cities'].split(", "):
#         notifications.send_email_alert()
