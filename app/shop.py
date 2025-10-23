import json
import math


class Shop:
    def __init__(self, name: str, location: list[int]):
        self.name = name
        self.location = location


def create_shops(file_name):
    with open(file_name, "r") as file_read:
        read = json.load(file_read)

    shops = []

    for shop in read["shops"]:
        name_shop = Shop(shop["name"], shop["location"])

        name_shop.products = {}
        for name_product, value_product in shop["products"].items():
            name_shop.products[name_product] = value_product
        shops.append(name_shop)

    return shops

def distance(axis_1, axis_2):
    x_axis = axis_1[0] - axis_2[0]
    y_axis = axis_1[1] - axis_2[1]
    results = math.sqrt((x_axis**2) + (y_axis**2))
    return results
