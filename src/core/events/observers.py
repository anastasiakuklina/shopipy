from abc import ABC, abstractmethod

from .events import BaseEvent, EventEnum, PriceChangedEvent, ProductRestockedEvent


class IObserver(ABC):

    @abstractmethod
    def accept(self, event: BaseEvent):
        pass


class CustomerNotifier(IObserver):

    def accept(self, event: BaseEvent):
        match event.name:
            case EventEnum.price_changed:
                event: PriceChangedEvent
                print(f"Price of {event.product.name} changed from {event.old_price} to {event.product.price}")
            case EventEnum.product_restocked:
                event: ProductRestockedEvent
                print(f"Product {event.product.name} back in to stock")