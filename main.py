from src.countries import Country
from src.shipping import RegionStore, ShippingCalculator


def create_statement(values: list[tuple[str, float, float]]) -> str:
    return "\n".join(
        [f"Shipping cost to {v[0]} for order total £{v[1]} is £{v[2]}" for v in values]
    )


if __name__ == "__main__":
    calculator = ShippingCalculator(region_store=RegionStore())
    print(
        create_statement(
            [
                (
                    Country.UNITED_KINGDOM.value,
                    99.99,
                    calculator.calculate_shipping(Country.UNITED_KINGDOM.value, 99.99),
                ),
                (
                    Country.UNITED_KINGDOM.value,
                    100.00,
                    calculator.calculate_shipping(Country.UNITED_KINGDOM.value, 100.00),
                ),
                (
                    Country.FRANCE.value,
                    99.99,
                    calculator.calculate_shipping(Country.FRANCE.value, 99.99),
                ),
                (
                    Country.FRANCE.value,
                    100.00,
                    calculator.calculate_shipping(Country.FRANCE.value, 100.00),
                ),
                (
                    Country.ALBANIA.value,
                    99.99,
                    calculator.calculate_shipping(Country.ALBANIA.value, 99.99),
                ),
                (
                    Country.ALBANIA.value,
                    100.00,
                    calculator.calculate_shipping(Country.ALBANIA.value, 100.00),
                ),
            ]
        )
    )
