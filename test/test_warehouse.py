from src.product import Product
from src.warehouse import Warehouse


def test_warehouse() -> None:
    product = Product(id=3, description="product used for testing", price=6.5)

    warehouse = Warehouse([])
    warehouse.add_product_stock(product=product, amount_to_add=5)
    warehouse.reduce_product_stock(product=product, amount_to_remove=2)
    assert warehouse.get_product_stock(product=product) == 3
