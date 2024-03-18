import requests as requests

from src.countries import Country


class RegionStore:
    @staticmethod
    def get_region(country: Country) -> str:
        url = (
            "https://npovmrfcyzu2gu42pmqa7zce6a0zikbf.lambda-url.eu-west-2.on.aws/?country="
            + country.value
        )

        response = requests.get(url)
        response.raise_for_status()

        region = response.json()["region"]
        return region


class ShippingCalculator:
    def __init__(self, region_store: RegionStore) -> None:
        self._region_store = region_store

    def calculate_shipping(self, country: Country, order_total: float) -> float:
        region = self._region_store.get_region(country=country)
        shipping = 0.0

        if region == "UK":
            if order_total < 120.0:
                shipping = 4.99

        if region == "EU":
            if order_total < 100:
                shipping = 8.99
            else:
                shipping = 4.99

        if region == "OTHER":
            if order_total >= 200:
                shipping = 5.99
            else:
                shipping = 9.99

        return shipping
