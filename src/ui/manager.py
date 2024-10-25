from enum import Enum

from src.core import ProductEnum, ClothingParams, ApplianceParams, ProductData
from .common import request_product_name, request_product_quantity


class ManagerActions(Enum):
    add_product = 1
    add_quantity = 2
    display_products = 3
    switch = 4
    exit = 5


def request_product_price():
    return float(input("Введите цену товара: "))


def request_manager_action() -> ManagerActions:
    while True:
        try:
            action = int(input(f"Выберите действие: \n1. Добавить товар \n2. Добавить количество товаров \n3. Просмотреть товары "
                               f"\n4. Перейти в режим клиента\n5. Выйти\n"))
            return ManagerActions(action)
        except ValueError:
            print(f"Режим должен быть от 1 до {len(ManagerActions)}")


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
    typ = request_product_type()
    name = request_product_name()
    price = request_product_price()
    match typ:
        case ProductEnum.clothing:
            params = request_clothing_info()
        case ProductEnum.appliance:
            params = request_appliance_info()
        case _:
            raise Exception("Неизвестный тип продукта")
    quantity = request_product_quantity()
    return ProductData(typ, name, price, params), quantity
