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


def add_item_to_order(order: Order, warehouse: Warehouse, item: Item) -> None:
    order.items.append(item)
    warehouse.reduce_product_stock(product=item.product, amount_to_remove=item.quantity)
