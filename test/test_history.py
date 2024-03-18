from src.address import Address
from src.countries import Country
from src.history import SalesHistory
from src.order import Item, Order
from src.product import Product


def test_get_orders_containing_product_returns_correct_orders() -> None:
    address = Address(
        house="mock_house",
        street="mock_street",
        city="mock_city",
        postcode="MOCK POSTCODE",
        country=Country.UNITED_KINGDOM,
    )

    expected_product = Product(id=1, description="type 1", price=5.0)

    expected_order = Order(
        shipping_address=address,
        items=[
            Item(Product(id=4, description="type 2", price=7.5), quantity=10),
            Item(Product(id=5, description="type 3", price=3.1), 12),
            Item(expected_product, quantity=1),
        ],
    )
    other_order = Order(
        shipping_address=address,
        items=[
            Item(Product(id=4, description="type 2", price=7.5), quantity=6),
            Item(Product(id=5, description="type 3", price=3.1), 9),
        ],
    )

    history = SalesHistory(orders=[expected_order, other_order])
    assert history.get_orders_containing_product(product=expected_product) == [
        expected_order
    ]
