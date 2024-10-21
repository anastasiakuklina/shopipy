from src.controller import Controller


def request_product_name():
    return input("Введите название товара: ")


def request_product_price():
    return float(input("Введите цену товара: "))


def request_product_quantity():
    return int(input("Введите количество товара: "))


def main():
    controller = Controller()
    while True:
        print("1. Добавить товар\n2. Просмотреть товары\n3. Купить товар\n4. Просмотреть корзину\n5. Выйти")
        choice = input("Выберите действие: ")
        if choice == "1":
            name = request_product_name()
            price = request_product_price()
            quantity = request_product_quantity()
            controller.add_product(name, price, quantity)
        elif choice == "2":
           controller.display_store_products()
        elif choice == "3":
            name = request_product_name()
            quantity = request_product_quantity()
            controller.buy_product(name, quantity)
        elif choice == "4":
            controller.display_cart()
        elif choice == "5":
            break
        else:
            print("Неверный ввод, попробуйте снова.")


if __name__ == "__main__":
    main()
