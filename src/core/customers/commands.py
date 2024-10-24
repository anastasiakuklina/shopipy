from abc import ABC, abstractmethod

from src.core.customers.carts import Cart
from src.core.products.abstract import IProduct


class ICommand(ABC):

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class AddProductCommand(ICommand):

    def __init__(self, cart: Cart, product: IProduct, quantity: int):
        self.cart = cart
        self.product = product
        self.quantity = quantity

    def execute(self):
        self.cart.add_product(self.product, self.quantity)

    def undo(self):
        self.cart.remove_product(self.product, self.quantity)