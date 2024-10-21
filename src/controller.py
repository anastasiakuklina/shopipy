from src.core.customers import Customer
from src.core.store import Store


class Controller:

    def __init__(self):
        self.store = Store()
        self.customer = Customer("John", self.store)
        self.store.add_product("apple", 100, 20)

    def add_product(self, name: str, price: float, quantity: int):
        self.store.add_product(name, price, quantity)

    def display_store_products(self):
        self.store.display_products()

    def buy_product(self, name: str, quantity: int):
        product = self.store.get_product(name)
        if not product:
            print("Такого продукта не существует")
            return
        self.customer.buy_product(product, quantity)

    def display_cart(self):
        self.customer.display_cart()
