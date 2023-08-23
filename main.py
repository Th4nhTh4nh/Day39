# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
from data_manager import DataManager
from pprint import pprint

sheety_endpoint = (
    "https://api.sheety.co/b3ee87d266692ec6590e617dcc1188d0/flightDeals/prices"
)

data_manager = DataManager()
sheet_data = data_manager.get_airport_data()
pprint(sheet_data)

for row in sheet_data:
    if row["iataCode"] == "":
        from flight_search import FlightSearch

        flight_search = FlightSearch()
        row["iataCode"] = flight_search.get_airport_code(row["city"])
pprint(sheet_data)

data_manager.airport_data = sheet_data
data_manager.update_airport_code()
