from dataclasses import dataclass

from src.address import Address
from src.product import Product


@dataclass
class Item:
    product: Product
    quantity: int


@dataclass
class Order:
    shipping_address: Address
    items: list[Item]
