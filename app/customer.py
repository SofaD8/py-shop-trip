import math
from typing import Dict, List
from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: Dict[str, int],
            location: List[int],
            money: float, car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car
        self.home_location = location[:]

    def distance_to(self, shop: Shop) -> float:
        return math.sqrt(
            (self.location[0] - shop.location[0])**2
            + (self.location[1] - shop.location[1])**2
        )

    def trip_cost(self, shop: Shop, fuel_price: float) -> float:
        dist = self.distance_to(shop)
        fuel_to_shop = self.car.fuel_cost(dist, fuel_price)
        fuel_back = self.car.fuel_cost(dist, fuel_price)
        products_cost = shop.calculate_cart_cost(self.product_cart)
        return round(fuel_to_shop + products_cost + fuel_back, 2)

    def go_shopping(self, shop: Shop, fuel_price: float) -> None:
        trip_cost = self.trip_cost(shop, fuel_price)
        print(f"{self.name}'s trip to {shop.name} costs {trip_cost}")

        if self.money >= trip_cost:
            print(f"{self.name} rides to {shop.name}")
            self.location = shop.location[:]
            shop.print_receipt(self.name, self.product_cart)
            self.location = self.home_location[:]
            self.money -= trip_cost
            print(f"{self.name} rides home")
            print(f"{self.name} now has {round(self.money, 2)} dollars\n")
        else:
            print(f"{self.name} doesn't have enough money"
                  f" to make a purchase in any shop\n")
