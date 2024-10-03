class FlightData:

    def __init__(self):
        self.stops = 0

    def find_cheapest_option(self, data):
        cheapest_flight = None
        for flight in data['data']:
            if not cheapest_flight:
                cheapest_flight = flight
            elif cheapest_flight['price']['grandTotal'] > flight['price']['grandTotal']:
                cheapest_flight = flight
        airport = cheapest_flight['itineraries'][1]['segments'][0]['arrival']['iataCode']
        if cheapest_flight['itineraries'][0]['segments'][0]['departure']['iataCode'] != airport:
            self.stops = len(cheapest_flight['itineraries']) - 1
        return [cheapest_flight, self.stops]
