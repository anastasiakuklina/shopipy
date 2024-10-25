from abc import ABC, abstractmethod

from .carts import Cart
from src.core.products import IProduct


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