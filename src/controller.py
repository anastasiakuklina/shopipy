from result import Result, Err, Ok

from src.core.customers.customers import Customer
from src.core.events.observers import CustomerNotifier
from src.core.products.abstract import IProduct
from src.core.products.appliance import ApplianceProductFactory
from src.core.products.clothing import ClothingProductFactory, ClothingParams
from src.core.store import Store
from src.data_input import ProductEnum, ProductData


class Controller:

    def __init__(self):
        self.store = Store()
        self.customers = {}
        self.customer = None
        self.store.attach(CustomerNotifier())
        cloth_params = ClothingParams("S", "jeans")
        product = ClothingProductFactory().create_product("jeans", 1000, cloth_params)
        self.store.add_product(product, 10)

    def set_current_customer(self, name: str):
        if name in self.customers:
            self.customer = self.customers[name]
        else:
            self.customer = Customer(name, self.store)
            self.customers[name] = self.customer

    def add_product(self, product_data: ProductData, quantity: int) -> Result[IProduct, str]:
        match product_data.typ:
            case ProductEnum.clothing:
                product = ClothingProductFactory().create_product(product_data.name, product_data.price, product_data.params)
            case ProductEnum.appliance:
                product = ApplianceProductFactory().create_product(product_data.name, product_data.price, product_data.params)
            case _:
                return Err("Нет фабричного метода для этого продукта")
        return self.store.add_product(product, quantity)

    def add_clothing_product(self, name: str, price: float, clothing_params: ClothingParams, quantity: int):
        product = ClothingProductFactory().create_product(name, price, params=clothing_params)
        self.store.add_product(product, quantity)

    def display_store_products(self):
        self.store.display_products()

    def buy_product(self, name: str, quantity: int) -> Result[None, str]:
        product = self.store.get_product(name)
        if not product:
            return Err("Такого продукта не существует")
        return self.customer.buy_product(product, quantity)

    def add_quantity(self, name: str, quantity: int) -> Result[None, str]:
        product = self.store.get_product(name)
        if not product:
            return Err("Такого продукта не существует")
        self.store.add_quantity(product, quantity)
        return Ok(None)

    def cancel_last_customer_action(self):
        self.customer.cancel_last_command()

    def display_cart(self):
        self.customer.display_cart()
