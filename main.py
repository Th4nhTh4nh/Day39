from data_manager import DataManager
from pprint import pprint
from flight_search import FlightSearch
import datetime


ORIGIN_CITY_IATA = "LON"
tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
six_month_from_today = datetime.datetime.now() + datetime.timedelta(days=6 * 30)

sheety_endpoint = (
    "https://api.sheety.co/b3ee87d266692ec6590e617dcc1188d0/flightDeals/prices"
)

flight_search = FlightSearch()
data_manager = DataManager()
sheet_data = data_manager.get_airport_data()
pprint(sheet_data)

for row in sheet_data:
    if row["iataCode"] == "":
        from flight_search import FlightSearch

        # flight_search = FlightSearch()
        row["iataCode"] = flight_search.get_airport_code(row["city"])
pprint(sheet_data)
data_manager.airport_data = sheet_data
data_manager.update_airport_code()

for destination in sheet_data:
    flight = flight_search.check_flight(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today,
    )
