from result import is_err

from src.controller import Controller
from src.ui import Mode, request_product_name, request_product_quantity, request_mode
from src.ui import CustomerActions, request_customer_action, request_customer_name
from src.ui import ManagerActions, request_manager_action, request_product_data_and_quantity


def run_manager_mode(controller: Controller):
    while True:
        action = request_manager_action()
        match action:
            case ManagerActions.add_product:
                product_data, quantity = request_product_data_and_quantity()
                res = controller.add_product(product_data, quantity)
                print(res.err_value) if is_err(res) else None
            case ManagerActions.add_quantity:
                name = request_product_name()
                quantity = request_product_quantity()
                res = controller.add_quantity(name, quantity)
                print(res.err_value) if is_err(res) else None
            case ManagerActions.display_products:
                controller.display_store_products()
            case ManagerActions.switch:
                return Mode.customer
            case ManagerActions.exit:
                return Mode.exit


def run_customer_mode(controller: Controller):
    name = request_customer_name()
    controller.set_current_customer(name)
    while True:
        action = request_customer_action()
        match action:
            case CustomerActions.buy_product:
                name = request_product_name()
                quantity = request_product_quantity()
                res = controller.buy_product(name, quantity)
                print(res.err_value) if is_err(res) else None
            case CustomerActions.undo_action:
                controller.cancel_last_customer_action()
            case CustomerActions.display_cart:
                controller.display_cart()
            case CustomerActions.display_products:
                controller.display_store_products()
            case CustomerActions.switch:
                return Mode.manager
            case CustomerActions.exit:
                return Mode.exit


def main():
    controller = Controller()
    mode = request_mode()
    while True:
        match mode:
            case Mode.manager:
                mode = run_manager_mode(controller)
            case Mode.customer:
                mode = run_customer_mode(controller)
            case Mode.exit:
                break


if __name__ == "__main__":
    main()
