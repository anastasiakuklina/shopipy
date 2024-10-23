from abc import ABC, abstractmethod


class IProduct(ABC):

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    @abstractmethod
    def __str__(self):
        pass


class IProductFactory(ABC):

    @abstractmethod
    def create_product(self, name: str, price: float, params) -> IProduct:
        pass


