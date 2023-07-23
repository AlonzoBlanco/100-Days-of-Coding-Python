from coffee_maker import CoffeeType, CoffeeMaker


# Function to ask the user the coffee type

def coffee_option():
    while True:
        coffee = input("What would you like to order? (espresso/latte/cappuccino): ").lower()
        if coffee in ["espresso", "latte", "cappuccino"]:
            return coffee
        else:
            print("Please select a valid option\n")
# end coffee_option


def main():
    coffee_machine = CoffeeMaker()
    coffee_types = CoffeeType()
    while True:
        print(f"Coffee machine report: {coffee_machine.report()}\n")
        selected_coffee = coffee_option()
        


        # selected_coffee_obj = coffee_types.ingredients[selected_coffee]
        # print(f"DEV COMMENT {selected_coffee_obj}")
        #
        # if coffee_machine.is_resource_sufficient(selected_coffee_obj["ingredients"]):
        #     coffee_machine.make_coffee(selected_coffee)


if __name__ == '__main__':
    main()
