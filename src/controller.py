from result import Result, Err, Ok

from src.core import  (
    Store,
    ClothingParams,
    CustomerNotifier,
    ClothingProductFactory,
    Customer,
    ProductEnum,
    ProductData,
    IProduct,
    ApplianceProductFactory
)


class Controller:

    def __init__(self):
        self.store = Store()
        self.customers = {}
        self.current_customer = None
        self.store.attach(CustomerNotifier())
        self.load_product()

    def load_product(self):
        cloth_params = ClothingParams("S", "grey")
        product = ClothingProductFactory().create_product("jeans", 1000, cloth_params)
        self.store.add_product(product, 10)

    def set_current_customer(self, name: str):
        if name in self.customers:
            self.current_customer = self.customers[name]
        else:
            self.current_customer = Customer(name, self.store)
            self.customers[name] = self.current_customer

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
        return self.current_customer.buy_product(product, quantity)

    def add_quantity(self, name: str, quantity: int) -> Result[None, str]:
        product = self.store.get_product(name)
        if not product:
            return Err("Такого продукта не существует")
        self.store.add_quantity(product, quantity)
        return Ok(None)

    def cancel_last_customer_action(self):
        self.current_customer.cancel_last_command()

    def display_cart(self):
        self.current_customer.display_cart()
