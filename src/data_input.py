from dataclasses import dataclass
from enum import Enum

from src.core.products.appliance import ApplianceParams
from src.core.products.clothing import ClothingParams


class ProductEnum(Enum):
    clothing = 1
    appliance = 2


@dataclass
class ProductData:
    typ: ProductEnum
    name: str
    price: float
    params: ClothingParams | ApplianceParams


def request_product_name():
    return input("Введите название товара: ")


def request_product_price():
    return float(input("Введите цену товара: "))


def request_product_quantity():
    return int(input("Введите количество товара: "))


def request_product_type() -> ProductEnum:
    while True:
        try:
            product_type = int(input(f"Выберите тип товара: {ProductEnum.clothing.value} одежда, {ProductEnum.appliance.value} техника: "))

            return ProductEnum(product_type)
        except ValueError:
            print("Тип продукта должен быть 1 или 2")


def request_clothing_info() -> ClothingParams:
    size = input("Введите размер: ")
    color = input("Введите цвет: ")
    return ClothingParams(size=size, color=color)


def request_appliance_info() -> ApplianceParams:
    model = input("Введите модель техники: ")
    power = int(input("Введите мощность: "))
    return ApplianceParams(model=model, power=power)


def request_product_data_and_quantity() -> tuple[ProductData, int]:
    name = request_product_name()
    price = request_product_price()
    typ = request_product_type()
    match typ:
        case ProductEnum.clothing:
            params = request_clothing_info()
        case ProductEnum.appliance:
            params = request_appliance_info()
        case _:
            raise Exception("Неизвестный тип продукта")
    quantity = request_product_quantity()
    return ProductData(typ, name, price, params), quantity