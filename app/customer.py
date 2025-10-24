from app.car import Car


class Customer:
    def __init__(
            self,
            name: str,
            money: float,
            used_fuel_in_dollars: float,
            location: list[int]
    ) -> None:
        self.name = name
        self.money = money
        self.used_fuel_in_dollars = used_fuel_in_dollars
        self.location = location


def make_customer_from_json_file(file_name: str) -> list[object]:
    customers = []
    for customer in file_name["customers"]:

        fuel_price = file_name.get("FUEL_PRICE", 0)
        fuel_consumption_in_dollars = (
            fuel_price * customer["car"]["fuel_consumption"]
        )

        new_customer = (
            Customer(
                customer["name"],
                customer["money"],
                fuel_consumption_in_dollars, customer["location"]
            )
        )
        new_customer.product_carts = customer.get("product_cart", 0)
        customers.append(new_customer)

        brand = customer["car"].get("brand", None)
        fuel_consumption = customer["car"].get("fuel_consumption", None)

        new_customer.car = Car(brand, fuel_consumption)
    return customers
