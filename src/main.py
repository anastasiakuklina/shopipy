from result import is_ok, is_err

from src.controller import Controller
from src.data_input import request_product_name, request_product_quantity, request_product_data_and_quantity


def main():
    controller = Controller()
    while True:
        print("1. Добавить товар \n2. Просмотреть товары\n3. Купить товар"
              "\n4. Просмотреть корзину \n5. Добавить количество товаров \n6. Выйти")
        choice = input("Выберите действие: ")
        if choice == "1":
            product_data, quantity = request_product_data_and_quantity()
            res = controller.add_product(product_data, quantity)
            print(res.err_value) if is_err(res) else None
        elif choice == "2":
           controller.display_store_products()
        elif choice == "3":
            name = request_product_name()
            quantity = request_product_quantity()
            res = controller.buy_product(name, quantity)
            print(res.err_value) if is_err(res) else None
        elif choice == "4":
            controller.display_cart()
        elif choice == "5":
            name = request_product_name()
            quantity = request_product_quantity()
            res = controller.add_quantity(name, quantity)
            print(res.err_value) if is_err(res) else None
        elif choice == "6":
            break
        else:
            print("Неверный ввод, попробуйте снова.")


if __name__ == "__main__":
    main()
