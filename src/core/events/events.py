from abc import abstractmethod
from enum import StrEnum

from src.core.products import IProduct


class EventEnum(StrEnum):
    price_changed = "price_changed"
    product_restocked = "product_restocked"


class BaseEvent:

    @property
    @abstractmethod
    def name(self) -> EventEnum:
        pass


class PriceChangedEvent(BaseEvent):
    name = EventEnum.price_changed

    def __init__(self, product: IProduct, old_price: float):
        self.product = product
        self.old_price = old_price


class ProductRestockedEvent(BaseEvent):
    name = EventEnum.product_restocked

    def __init__(self, product: IProduct):
        self.product = product
