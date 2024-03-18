from dataclasses import dataclass
from src.product import Product


@dataclass
class Entry:
    product: Product
    stock: int


@dataclass
class Warehouse:
    catalogue: list[Entry]

    def get_product_stock(self, product: Product) -> int:
        entry = next((e for e in self.catalogue if e.product == product), None)
        if entry is None:
            return 0
        return entry.stock

    def reduce_product_stock(self, product: Product, amount_to_remove: int) -> None:
        entry = next(e for e in self.catalogue if e.product == product)
        entry.stock = entry.stock - amount_to_remove

    def add_product_stock(self, product: Product, amount_to_add: int) -> None:
        entry = next((e for e in self.catalogue if e.product == product), None)
        if entry is not None:
            entry.stock = entry.stock + amount_to_add
            return
        self.catalogue.append(Entry(product=product, stock=amount_to_add))
