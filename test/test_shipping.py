from src.countries import Country
from src.shipping import RegionStore, ShippingCalculator
import pytest


class MockRegionStore(RegionStore):
    @staticmethod
    def get_region(country: str) -> str:
        return {"United Kingdom": "UK", "France": "EU"}.get(country, "OTHER")


@pytest.mark.parametrize(
    "country, order_total, cost",
    [
        (Country.UNITED_KINGDOM.value, 99.99, 4.99),
        (Country.UNITED_KINGDOM.value, 100.00, 0.0),
        (Country.FRANCE.value, 99.99, 8.99),
        (Country.FRANCE.value, 100.00, 4.99),
        (Country.ALBANIA.value, 99.99, 9.99),
        (Country.ALBANIA.value, 100.00, 9.99),
    ],
)
def test_calculate_shipping(country: str, order_total: float, cost: float) -> None:
    calculator = ShippingCalculator(region_store=MockRegionStore())
    assert (
        calculator.calculate_shipping(country=country, order_total=order_total) == cost
    )
