from enum import Enum


class Mode(Enum):
    manager = 1
    customer = 2
    exit = 3


def request_product_name():
    return input("Введите название товара: ")


def request_product_quantity():
    return int(input("Введите количество товара: "))


def request_mode() -> Mode:
    while True:
        try:
            mode = int(input(f"Выберите режим: \n1. менеджер \n2. покупатель \n3. Выйти \n"))
            return Mode(mode)
        except ValueError:
            print("Режим должен быть 1 или 2 или 3")
