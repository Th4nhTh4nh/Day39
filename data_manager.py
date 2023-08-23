import requests
from pprint import pprint

sheety_endpoint = (
    "https://api.sheety.co/b3ee87d266692ec6590e617dcc1188d0/flightDeals/prices"
)


class DataManager:
    def __init__(self) -> None:
        self.airport_data: dict = {}

    def get_airport_data(self):
        data = requests.get(url=sheety_endpoint).json()
        # pprint(data)
        self.airport_data = data["prices"]
        # print(type(data["prices"]))
        return self.airport_data

    def update_airport_code(self):
        for city in self.airport_data:
            new_data = {"price": {"iataCode": city["iataCode"]}}
            response = requests.put(
                url=f"{sheety_endpoint}/{city['id']}", json=new_data
            )
            print(response.text)
