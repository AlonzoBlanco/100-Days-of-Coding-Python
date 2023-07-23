
class CoffeeType:
    def __init__(self):
        self.ingredients = {
            "espresso": {
                "ingredients": {
                    "water": 50,
                    "coffee": 18,
                },
                "cost": 1.5,
            },
            "latte": {
                "ingredients": {
                    "water": 200,
                    "milk": 150,
                    "coffee": 24,
                },
                "cost": 2.5,
            },
            "cappuccino": {
                "ingredients": {
                    "water": 250,
                    "milk": 100,
                    "coffee": 24,
                },
                "cost": 3.0,
            }
        }


class CoffeeMaker:
    """Models the machine that makes the coffee"""
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }  # Dictionary

    def report(self):
        """Prints a report of all resources"""
        print(f"Water: {self.resources['water']} ml")
        print(f"Milk: {self.resources['milk']} ml")
        print(f"Coffee: {self.resources['coffee']}")

    def is_resource_sufficient(self, drink):
        """Returns True when order can be made, False if ingredients are insufficient"""
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make

    def make_coffee(self, order):
        """Deducts the required ingredients from the resources"""
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
            print(f"Here is your {order.name}. Enjoy")

### END OBJ Archive ###

import coffee_maker


def coffee_option():
    while True:
        coffee = input("What would you like to order? (espresso/latte/cappuccino): ").lower()
        if coffee in ["espresso", "latte", "cappuccino"]:
            return coffee
        else:
            print("Please select a valid option\n")
# end coffee_option


def main():
    coffee_machine = coffee_maker.CoffeeMaker()
    coffee_types = coffee_maker.CoffeeType()
    while True:
        coffee_machine.report()
        selected_coffee = coffee_option()

        selected_coffee_obj = coffee_types.ingredients[selected_coffee]
        print(f"DEV COMMENT {selected_coffee_obj}")
        
        if coffee_machine.is_resource_sufficient(selected_coffee_obj["ingredients"]):
            coffee_machine.make_coffee(selected_coffee)


if __name__ == '__main__':
    main()
