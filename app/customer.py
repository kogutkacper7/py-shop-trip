import json
from app.car import Car, cost_of_road

class Customer:
    def __init__(self, name: str, money: float, used_fuel_in_dollars: float, location: list[int]) -> None:
        self.name = name
        self.money = money
        self.used_fuel_in_dollars = used_fuel_in_dollars
        self.location = location


def make_customer_from_json_file(file_name):
    with open(file_name, "r") as file:
        file_read = json.load(file)
    customers = []
    for customer in file_read["customers"]:

        fuel_price = file_read.get("FUEL_PRICE", 0)
        used_fuel = {}
        fuel_consumption_in_dollars = fuel_price * customer["car"]["fuel_consumption"]
        used_fuel[customer["name"]] = fuel_consumption_in_dollars

        #creating object
        new_customer = Customer(customer["name"], customer["money"], fuel_consumption_in_dollars, customer["location"])

        #adding pruduct_carts to object
        new_customer.product_carts = customer.get("product_cart", 0)


        #products from product cart
        new_customer.products_price_list = {}
        for name_product, value_product in customer["product_cart"].items():
            new_customer.products_price_list[name_product] = value_product
        customers.append(new_customer)

        for car, value in customer["car"].items():
            if car == "brand":
                brand = value

            if car == "fuel_consumption":
                fuel_consumption = value

        new_customer.car = Car(brand, fuel_consumption)


    return customers
