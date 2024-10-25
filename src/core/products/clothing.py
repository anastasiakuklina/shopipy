from dataclasses import dataclass

from .abstract import IProduct, IProductFactory


@dataclass
class ClothingParams:
    size: str
    color: str


class ClothingProduct(IProduct):

    def __init__(self, name: str, price: float, size: str, color: str):
        super().__init__(name, price)
        self.size = size
        self.color = color

    def __str__(self):
        return f"{self.name} {self.price} руб. размер: {self.size} цвет: {self.color}"


class ClothingProductFactory(IProductFactory):

    def create_product(self, name: str, price: float, params: ClothingParams) -> ClothingProduct:
        return ClothingProduct(name, price, params.size, params.color)
