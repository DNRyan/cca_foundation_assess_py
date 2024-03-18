from dataclasses import dataclass
from src.address import Address
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

    def get_orders_with_address(self, address: Address) -> list[Order]:
        return [o for o in self.orders if o.shipping_address == address]
