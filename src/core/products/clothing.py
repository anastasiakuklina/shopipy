from dataclasses import dataclass

from src.core.products.abstract import Product, ProductFactory


@dataclass
class ClothingParams:
    size: str
    color: str


class ClothingProduct(Product):

    def __init__(self, name: str, price: float, size: str, color: str):
        super().__init__(name, price)
        self.size = size
        self.color = color

    def __str__(self):
        return f"{self.name} {self.price} руб. размер: {self.size} цвет: {self.color}"


class ClothingProductFactory(ProductFactory):

    def create_product(self, name: str, price: float, params: ClothingParams) -> ClothingProduct:
        return ClothingProduct(name, price, params.size, params.color)
