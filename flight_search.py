import requests
from pprint import pprint
from datetime import datetime, 

kiwi_server = "https://api.tequila.kiwi.com/"
kiwiapi_key = "dlzJSnpNGaoNvhBM6g59sPguh5PckO--"


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def get_airport_code(self, city):
        header = {"apikey": kiwiapi_key}
        params = {
            "term": city,
            "location_type": "airport",
        }
        response = requests.get(
            url=f"{kiwi_server}locations/query", headers=header, params=params
        )
        data = response.json()
        code = data["locations"][0]["code"]
        return code

    def check_flight(self, origin_city_code, destination_city_code, from_time, to_time):
        header = {"apikey": kiwiapi_key}
        params = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP",
        }

        response = requests.get(url=f"{kiwi_server}v2/search", headers=header, params=params)
