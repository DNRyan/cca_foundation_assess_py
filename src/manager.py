from src.history import SalesHistory
from src.order import Item, Order
from src.shipping import ShippingCalculator
from src.warehouse import Warehouse


class OrderManager:
    def __init__(
        self,
        history: SalesHistory,
        warehouse: Warehouse,
        shipping_calculator: ShippingCalculator,
        order: Order,
    ) -> None:
        self._history: SalesHistory = history
        self._warehouse: Warehouse = warehouse
        self._shipping: ShippingCalculator = shipping_calculator
        self._order: Order = order

    def add_item(self, item: Item) -> None:
        available_stock = self._warehouse.get_product_stock(product=item.product)
        if available_stock < item.quantity:
            raise ValueError("Required stock not available for product")

        self._order.items.append(item)

    def calculate_total(self) -> float:
        order_total = sum(
            [item.quantity * item.product.price for item in self._order.items]
        )
        shipping_cost = self._shipping.calculate_shipping(
            self._order.shipping_address.country.value, order_total
        )
        return order_total + shipping_cost

    def confirm(self) -> None:
        for item in self._order.items:
            self._warehouse.reduce_product_stock(
                product=item.product, amount_to_remove=item.quantity
            )
        self._history.orders.append(self._order)
