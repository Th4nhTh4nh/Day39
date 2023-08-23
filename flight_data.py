import requests
import datetime
from pprint import pprint

kiwi_server = "https://api.tequila.kiwi.com/"
kiwiapi_key = "dlzJSnpNGaoNvhBM6g59sPguh5PckO--"

tomorow_date = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime(
    "%d/%m/%Y"
)
six_months_late_date = (
    datetime.datetime.now() + datetime.timedelta(days=6 * 30)
).strftime("%d/%m/%Y")


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(
        self,
        price,
        origin_city,
        origin_airport,
        destination_city,
        destination_airport,
        out_date,
        return_date,
    ) -> None:
        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date


"""
    def get_price(self, city):
        header = {"apikey": kiwiapi_key}
        params = {
            "fly_from": self.departure_airport_code,
            "fly_to": city,
            "date-from": tomorow_date,
            "date_to": six_months_late_date,
            "curr": "GBP",
        }
        response = requests.get(
            url=f"{kiwi_server}search", headers=header, params=params
        )
        data = response.json()
        print(data["data"]["price"])

    pass
"""