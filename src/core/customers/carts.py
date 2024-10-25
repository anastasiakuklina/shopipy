from .calculators import ICalculator
from src.core.products import IProduct


class Cart:

    def __init__(self, calculator: ICalculator):
        self._calculator = calculator
        self.items = {}

    def add_product(self, product: IProduct, quantity: int):
        init_dict = {"product": product, "quantity": 0}
        self.items.setdefault(product.name, init_dict)["quantity"] += quantity

    def remove_product(self, product: IProduct, quantity: int):
        self.items[product.name]["quantity"] -= quantity
        if self.items[product.name]["quantity"] == 0:
            del self.items[product.name]

    def display_cart(self):
        for item in self.items.values():
            print(f"{item['product']} {item['quantity']} шт.")
        total = self.calculate_total()
        print(f"Итого: {total}")

    def calculate_total(self) -> float:
        return self.calculator.get_total(self.items)

    @property
    def calculator(self) -> ICalculator:
        return self._calculator

    @calculator.setter
    def calculator(self, calculator: ICalculator) -> None:
        self._calculator = calculator