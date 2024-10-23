from dataclasses import dataclass

from src.core.products.abstract import IProduct, IProductFactory


@dataclass
class ApplianceParams:
    model: str
    power: int


class ApplianceProduct(IProduct):

    def __init__(self, name: str, price: float, model: str, power: int):
        super().__init__(name, price)
        self.model = model
        self.power = power

    def __str__(self):
        return f"{self.name} {self.price} руб. модель: {self.model} мощность: {self.power}"


class ApplianceProductFactory(IProductFactory):

    def create_product(self, name: str, price: float, params: ApplianceParams) -> ApplianceProduct:
        return ApplianceProduct(name, price, params.model, params.power)
