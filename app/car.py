class Car:
    def __init__(self, brand, fuel_consumption):
        self.brand = brand
        self.fuel_consumption = fuel_consumption


def cost_of_road(used_fuel_in_dollars_per_100km: float, distance_to_shop: float) -> float:
    cost_of_road_in_both_ways = (used_fuel_in_dollars_per_100km * distance_to_shop) / 100
    return cost_of_road_in_both_ways
