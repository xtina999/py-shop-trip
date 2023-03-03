import json


class Customer:
    customers = []

    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: int,
            car: str) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    @classmethod
    def add_to_customers(cls) -> None:
        with open("app/config.json", "rb") as customers_file:
            customer_data = json.load(customers_file)
            for customer in customer_data["customers"]:
                for key, value in customer.items():
                    if key == "car":
                        brand = value["brand"]
                customer = cls(
                    name=customer["name"],
                    product_cart=customer["product_cart"],
                    location=customer["location"],
                    money=customer["money"],
                    car=brand,
                )

                cls.customers.append(customer)