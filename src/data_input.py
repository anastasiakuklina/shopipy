from dataclasses import dataclass
from enum import Enum

from src.core.products.appliance import ApplianceParams
from src.core.products.clothing import ClothingParams


class ProductEnum(Enum):
    clothing = 1
    appliance = 2


class Mode(Enum):
    manager = 1
    customer = 2
    exit = 3


class ManagerActions(Enum):
    add_product = 1
    add_quantity = 2
    display_products = 3
    switch = 4
    exit = 5


class CustomerActions(Enum):
    buy_product = 1
    undo_action = 2
    display_cart = 3
    display_products = 4
    switch = 5
    exit = 6


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


def request_mode() -> Mode:
    while True:
        try:
            mode = int(input(f"Выберите режим: \n1. менеджер \n2. покупатель \n3. Выйти \n"))
            return Mode(mode)
        except ValueError:
            print("Режим должен быть 1 или 2 или 3")


def request_manager_action() -> ManagerActions:
    while True:
        try:
            action = int(input(f"Выберите действие: \n1. Добавить товар \n2. Добавить количество товаров \n3. Просмотреть товары "
                               f"\n4. Перейти в режим клиента\n5. Выйти\n"))
            return ManagerActions(action)
        except ValueError:
            print(f"Режим должен быть от 1 до {len(ManagerActions)}")


def request_customer_action() -> CustomerActions:
    while True:
        try:
            action = int(input(f"Выберите действие: \n1. Купить товар \n2. Отменить действие \n3. Просмотреть корзину "
                               f"\n4. Просмотреть товары \n5. Перейти в режим менеджера \n6. Выйти\n"))
            return CustomerActions(action)
        except ValueError:
            print(f"Режим должен быть от 1 до {len(CustomerActions)}")


def request_customer_name():
    return input("Введите имя: ")


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