from src.countries import Country
from src.shipping import RegionStore, ShippingCalculator
import pytest


class MockRegionStore(RegionStore):
    @staticmethod
    def get_region(country: Country) -> str:
        return {Country.UNITED_KINGDOM: "UK", Country.FRANCE: "EU"}.get(
            country, "OTHER"
        )


@pytest.mark.parametrize(
    "country, order_total, cost",
    [
        (Country.UNITED_KINGDOM, 99.99, 4.99),
        (Country.UNITED_KINGDOM, 100.00, 4.99),
        (Country.UNITED_KINGDOM, 130.00, 0.0),
        (Country.FRANCE, 99.99, 8.99),
        (Country.FRANCE, 100.00, 4.99),
        (Country.ALBANIA, 99.99, 9.99),
        (Country.ALBANIA, 100.00, 9.99),
        (Country.ALBANIA, 210.00, 5.99),
    ],
)
def test_calculate_shipping(country: Country, order_total: float, cost: float) -> None:
    calculator = ShippingCalculator(region_store=MockRegionStore())
    assert (
        calculator.calculate_shipping(country=country, order_total=order_total) == cost
    )
