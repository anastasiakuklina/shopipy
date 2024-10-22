from src.core.customers import Customer
from src.core.products.abstract import Product
from src.core.products.appliance import ApplianceProductFactory
from src.core.products.clothing import ClothingProductFactory, ClothingParams
from src.core.store import Store
from src.data_input import ProductEnum, ProductData


class Controller:

    def __init__(self):
        self.store = Store()
        self.customer = Customer("John", self.store)
        cloth_params = ClothingParams("S", "jeans")
        product = ClothingProductFactory().create_product("jeans", 1000, cloth_params)
        self.store.add_product(product, 5)
        # self.store.add_product("apple", 100, 20)

    def add_product(self, product_data: ProductData, quantity: int):
        match product_data.typ:
            case ProductEnum.clothing:
                product = ClothingProductFactory().create_product(product_data.name, product_data.price, product_data.params)
            case ProductEnum.appliance:
                product = ApplianceProductFactory().create_product(product_data.name, product_data.price, product_data.params)
            case _:
                product = None
        if not product:
            return False
        self.store.add_product(product, quantity)

    def add_clothing_product(self, name: str, price: float, clothing_params: ClothingParams, quantity: int):
        product = ClothingProductFactory().create_product(name, price, params=clothing_params)
        self.store.add_product(product, quantity)

    def display_store_products(self):
        self.store.display_products()

    def buy_product(self, name: str, quantity: int):
        product = self.store.get_product(name)
        if not product:
            print("Такого продукта не существует")
            return
        self.customer.buy_product(product, quantity)

    def display_cart(self):
        self.customer.display_cart()
