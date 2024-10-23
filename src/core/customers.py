from src.core.carts import Cart
from src.core.products.abstract import IProduct
from src.core.store import Store


class Customer:

    def __init__(self, name: str, store: Store):
        self.name = name
        self.store = store
        self.cart = Cart()

    def buy_product(self, product: IProduct, quantity: int):
        if not self.store.has_enough_products(product, quantity):
            raise Exception("store doesn't have enough products to buy")

        self.store.reduce_quantity(product, quantity)
        self.cart.add_product(product, quantity)

    def display_cart(self):
        return self.cart.display_cart()