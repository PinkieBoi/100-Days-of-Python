from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
flight_search.get_oauth_token()
notifications = NotificationManager()

for city in data_manager.get_sheet()["prices"]:
    best_deal = flight_search.get_flight_offers(city['iataCode'], city['lowestPrice'], 7)
    if float(city['lowestPrice']) > float(best_deal['lowestPrice']):
        old_price = city['lowestPrice']
        data_manager.edit_sheet(best_deal['lowestPrice'], city['id'])
        price_alert = f"Flight to {city['city']} down form £{old_price} to £{best_deal['lowestPrice']}"
        notifications.send_alert(best_deal)
