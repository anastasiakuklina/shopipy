from result import Err, Result, Ok

from src.core.events import BaseEvent, IPublicator, IObserver, ProductRestockedEvent
from src.core.products import IProduct
from src.utils.singleton import SingletonMeta


class Store(IPublicator):

    def __init__(self):
        self.inventory = {}
        self.observers = []

    def add_product(self, product: IProduct, quantity: int) -> Result[None, str]:
        if  product.name in self.inventory:
            return Err("Такой продукт уже есть в магазине")
        self.inventory[product.name] = {"product": product, "quantity": quantity}
        return Ok(None)

    def get_product(self, name: str) -> IProduct | None:
        return self.inventory.get(name, {}).get("product")

    def has_enough_products(self, product: IProduct, quantity: int):
        return self.inventory[product.name]["quantity"] >= quantity

    def add_quantity(self, product: IProduct, quantity: int):
        old_quantity = self.inventory[product.name]["quantity"]
        self.inventory[product.name]["quantity"] += quantity
        if old_quantity == 0 and quantity > 0:
            event = ProductRestockedEvent(product)
            self.notify(event)

    def reduce_quantity(self, product: IProduct, quantity: int):
        self.inventory[product.name]["quantity"] -= quantity

    def display_products(self):
        for item in self.inventory.values():
            print(f"{item['product']} {item['quantity']} шт.")

    def attach(self, observer: IObserver) -> None:
        self.observers.append(observer)

    def detach(self, observer: IObserver) -> None:
        self.observers.remove(observer)

    def notify(self, event: BaseEvent) -> None:
        for observer in self.observers:
            observer.accept(event)