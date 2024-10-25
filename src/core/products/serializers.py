from dataclasses import dataclass
from enum import Enum

from .appliance import ApplianceParams
from .clothing import ClothingParams


class ProductEnum(Enum):
    clothing = 1
    appliance = 2


@dataclass
class ProductData:
    typ: ProductEnum
    name: str
    price: float
    params: ClothingParams | ApplianceParams
