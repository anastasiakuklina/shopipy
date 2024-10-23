from abc import ABC, abstractmethod

from src.core.events.events import BaseEvent
from src.core.events.observers import IObserver


class IPublicator(ABC):

    @abstractmethod
    def attach(self, observer: IObserver) -> None:
        pass

    @abstractmethod
    def detach(self, observer: IObserver) -> None:
        pass

    @abstractmethod
    def notify(self, event: BaseEvent) -> None:
        pass
