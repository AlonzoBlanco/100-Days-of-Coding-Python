#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ## ################################################################
# Date: 07/07/2023
# Name: "Coffe Machine"
# Author: Blanco Pulido Gabriel Alonzo
# License: MIT
# ## ################################################################

MENU = {
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def main():
    while True:
        option = "NULL"
        print(resources)
        while option not in ["espresso", "latte", "cappuccino"]:
            option = input("\nWhat would you like to order? (espresso/latte/cappuccino): ").lower()
            if option not in ["espresso", "latte", "cappuccino"]:
                print("Type a valid option, please\n")
            else:
                pass

        print("\nPlease insert coins.")
        coin_list = [["quarters", 0, 0.25], ["dimes", 0, 0.1], ["nickles", 0, 0.05], ["pennies", 0, 0.01]]
        total_amount = 0
        for i in range(len(coin_list)):
            coin_list[i][1] = int(input(f"How many {coin_list[i][0]}?: "))
            total_amount += coin_list[i][1] * coin_list[i][2]
        total_amount = round(total_amount, 2)

        if total_amount < MENU[option]["cost"]:
            print("Sorry that's not enough money. Money refunded.")
        elif resources["water"] < MENU[option]["ingredients"]["water"]:
            print("Sorry not enough water. Money refunded.")
        elif resources["coffee"] < MENU[option]["ingredients"]["coffee"]:
            print("Sorry not enough coffee. Money refunded.")
        elif option in ["latte", "cappuccino"] and resources["milk"] < MENU[option]["ingredients"]["milk"]:
            print("Sorry not enough milk. Money refunded.")
        else:
            change = total_amount - MENU[option]["cost"]
            if change > 0:
                print(f"Here is {change} in change\n")
            resources["water"] -= MENU[option]["ingredients"]["water"]
            resources["coffee"] -= MENU[option]["ingredients"]["coffee"]
            if option in ["latte", "cappuccino"]:
                resources["milk"] -= MENU[option]["ingredients"]["milk"]
            resources["money"] += MENU[option]["cost"]
            print(f"Here is your {option} ☕️. Enjoy!\n")

# end main


if __name__ == '__main__':
    main()
