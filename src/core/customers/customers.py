from random import randint
from typing import List

from result import Err, Result, Ok

from .carts import Cart
from .calculators import StandardCalculator, VIPCalculator
from .commands import AddProductCommand, ICommand
from src.core.products import IProduct
from src.core.store import Store


class Customer:

    def __init__(self, name: str, store: Store):
        self.name = name
        self.store = store
        self.cart = Cart(StandardCalculator())
        self.command_history: List[ICommand] = []

    def buy_product(self, product: IProduct, quantity: int) -> Result[None, str]:
        if not self.store.has_enough_products(product, quantity):
            return Err("store doesn't have enough products to buy")

        self.store.reduce_quantity(product, quantity)
        command = AddProductCommand(self.cart, product, quantity)
        command.execute()
        self.command_history.append(command)
        return Ok(None)

    def cancel_last_command(self):
        if not self.command_history:
            return
        command = self.command_history.pop()
        command.undo()

    def display_cart(self):
        calculator = VIPCalculator() if randint(0, 1) else StandardCalculator()
        self.cart.calculator = calculator
        return self.cart.display_cart()