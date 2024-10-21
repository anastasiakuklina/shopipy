from src.core.products import Product


class Cart:

    def __init__(self):
        self.items = {}

    def add_product(self, product: Product, quantity: int):
        init_dict = {"product": product, "quantity": 0}
        self.items.setdefault(product.name, init_dict)["quantity"] += quantity

    def display_cart(self):
        total = 0
        for item in self.items.values():
            print(f"{item['product']} {item['quantity']} шт.")
            total += item["product"].price * item["quantity"]
        print(total)
