import datetime
from typing import Dict


class Shop:
    def __init__(
            self,
            name: str,
            location: list,
            products: Dict[str, float]
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def calculate_cart_cost(self, cart: Dict[str, int]) -> float:
        total = 0
        for product, qty in cart.items():
            if product in self.products:
                total += self.products[product] * qty
        return total

    def print_receipt(
            self,
            customer_name: str,
            cart: Dict[str, int]
    ) -> None:
        date_str = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"\nDate: {date_str}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")
        total = 0
        for product, qty in cart.items():
            price = self.products[product] * qty
            if float(price).is_integer():
                price_str = str(int(price))
            else:
                price_str = str(price)
            print(f"{qty} {product}s for {price_str} dollars")
            total += price
        print(f"Total cost is {total} dollars")
        print("See you again!\n")
