from enum import Enum


class CustomerActions(Enum):
    buy_product = 1
    undo_action = 2
    display_cart = 3
    display_products = 4
    switch = 5
    exit = 6


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
