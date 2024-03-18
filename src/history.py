from dataclasses import dataclass
from src.order import Order
from src.product import Product


@dataclass
class SalesHistory:
    orders: list[Order]

    def get_orders_containing_product(self, product: Product) -> list[Order]:
        # TODO: turn this into a list comp
        def iter_orders_containing_product():
            for order in self.orders:
                if product in [item.product for item in order.items]:
                    yield order

        return list(iter_orders_containing_product())
