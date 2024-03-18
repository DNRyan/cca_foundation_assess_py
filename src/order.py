from dataclasses import dataclass

from src.address import Address
from src.product import Product
from src.warehouse import Warehouse


@dataclass
class Item:
    product: Product
    quantity: int


@dataclass
class Order:
    shipping_address: Address
    items: list[Item]

    def add_item(self, warehouse: Warehouse, item: Item) -> None:
        available_stock = warehouse.get_product_stock(product=item.product)
        if available_stock < item.quantity:
            raise ValueError("Required stock not available for product")

        self.items.append(item)
        warehouse.reduce_product_stock(product=item.product, amount_to_remove=item.quantity)
