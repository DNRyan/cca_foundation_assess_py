from src.warehouse import Warehouse, Entry
from src.order import Item, Order
from src.manager import OrderManager
from src.address import Address
from src.countries import Country
from src.product import Product
from test.test_shipping import MockRegionStore
from src.shipping import ShippingCalculator
from src.history import SalesHistory
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


@pytest.fixture
def mock_order_manager(mock_address: Address, mock_product: Product) -> OrderManager:
    return OrderManager(
        history=SalesHistory([]),
        warehouse=Warehouse([Entry(product=mock_product, stock=5)]),
        shipping_calculator=ShippingCalculator(MockRegionStore()),
        order=Order(mock_address, []),
    )


def test_add_item_to_order_successful_when_quantity_available_in_warehouse(
    mock_order_manager: OrderManager, mock_product: Product
) -> None:
    item = Item(product=mock_product, quantity=4)
    mock_order_manager.add_item(item=item)
    assert item in mock_order_manager._order.items


def test_add_item_to_order_throws_value_error_when_not_enough_stock_in_warehouse(
    mock_order_manager: OrderManager, mock_product: Product
) -> None:
    item = Item(product=mock_product, quantity=8)

    with pytest.raises(ValueError):
        mock_order_manager.add_item(item=item)


def test_calculate_total_returns_correct_value(
    mock_order_manager: OrderManager, mock_product: Product
) -> None:
    mock_order_manager._warehouse.catalogue = [Entry(product=mock_product, stock=6)]
    item = Item(product=mock_product, quantity=4)
    mock_order_manager.add_item(item=item)
    assert mock_order_manager.calculate_total() == 10.99
