from abc import ABC, abstractmethod


class ICalculator(ABC):

    @abstractmethod
    def get_total(self, items) -> float:
        pass


class StandardCalculator(ICalculator):

    def get_total(self, items) -> float:
        total = 0
        for item in items.values():
            total += item["product"].price * item["quantity"]
        return total


class VIPCalculator(ICalculator):
    vip_discount = 0.03

    def get_total(self, items) -> float:
        total = 0
        for item in items.values():
            total += item["product"].price * item["quantity"]
        return total * (1 - self.vip_discount)