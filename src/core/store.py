from src.core.products import Product
from src.utils.singleton import SingletonMeta


class Store(metaclass=SingletonMeta):

    def __init__(self):
        self.inventory = {}

    def add_product(self, name: str, price: float, quantity: int):
        # TODO проверить, что ещё не существует
        product = Product(name, price)
        self.inventory[name] = {"product": product, "quantity": quantity}

    def get_product(self, name: str) -> Product | None:
        return self.inventory.get(name, {}).get("product")

    def has_enough_products(self, product: Product, quantity: int):
        return self.inventory[product.name]["quantity"] >= quantity

    def reduce_quantity(self, product: Product, quantity: int):
        self.inventory[product.name]["quantity"] -= quantity

    def display_products(self):
        for item in self.inventory.values():
            print(f"{item['product']} {item['quantity']} шт.")