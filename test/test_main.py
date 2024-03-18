from src.countries import Country
from main import create_statement


def test_create_statement() -> None:
    assert (
        create_statement(
            [
                (Country.UNITED_KINGDOM.value, 99.99, 4.99),
                (Country.UNITED_KINGDOM.value, 100.00, 4.99),
                (Country.FRANCE.value, 99.99, 8.99),
                (Country.FRANCE.value, 100.00, 4.99),
                (Country.ALBANIA.value, 99.99, 9.99),
                (Country.ALBANIA.value, 100.00, 9.99),
            ]
        )
        == """Shipping cost to United Kingdom for order total £99.99 is £4.99
Shipping cost to United Kingdom for order total £100.0 is £4.99
Shipping cost to France for order total £99.99 is £8.99
Shipping cost to France for order total £100.0 is £4.99
Shipping cost to Albania for order total £99.99 is £9.99
Shipping cost to Albania for order total £100.0 is £9.99"""
    )
