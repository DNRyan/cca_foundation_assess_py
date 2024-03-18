from src.warehouse import Warehouse, Entry
from src.order import Item, Order
from src.address import Address
from src.countries import Country
from src.product import Product
from test.test_shipping import MockRegionStore
from src.shipping import ShippingCalculator
import pytest


@pytest.fixture
def mock_address() -> Address:
    return Address(
        house="mock_house",
        street="mock_street",
        city="mock_city",
        postcode="MOCK POSTCODE",
        country=Country.UNITED_KINGDOM,
    )


@pytest.fixture
def mock_product() -> Product:
    return Product(id=1, description="product used for testing", price=1.5)


def test_add_item_to_order_successful_when_quantity_available_in_warehouse_and_warehouse_updated(
    mock_address: Address, mock_product: Product
) -> None:
    warehouse = Warehouse(catalogue=[Entry(product=mock_product, stock=5)])
    order = Order(shipping_address=mock_address, items=[])
    item = Item(product=mock_product, quantity=4)

    order.add_item(warehouse=warehouse, item=item)
    assert warehouse.get_product_stock(product=mock_product) == 1
    assert item in order.items


def test_add_item_to_order_throws_value_error_when_not_enough_stock_in_warehouse(
    mock_address: Address, mock_product: Product
) -> None:
    warehouse = Warehouse(catalogue=[Entry(product=mock_product, stock=2)])
    order = Order(shipping_address=mock_address, items=[])
    item = Item(product=mock_product, quantity=4)

    with pytest.raises(ValueError):
        order.add_item(warehouse=warehouse, item=item)


def test_calculate_total_returns_correct_value(
    mock_address: Address, mock_product: Product
) -> None:
    warehouse = Warehouse(catalogue=[Entry(product=mock_product, stock=6)])
    order = Order(shipping_address=mock_address, items=[])
    item = Item(product=mock_product, quantity=4)
    order.add_item(warehouse=warehouse, item=item)
    
    shipping_calculator = ShippingCalculator(region_store=MockRegionStore())
    assert order.calculate_total(shipping_calculator=shipping_calculator) == 10.99
