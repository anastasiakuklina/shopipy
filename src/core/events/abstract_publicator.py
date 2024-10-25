from abc import ABC, abstractmethod

from .events import BaseEvent
from .observers import IObserver


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
