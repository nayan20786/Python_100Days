# Day 15
from pprint import pprint
# Coffee Machine Project

from Day15_Resources import MENU, resources
from art import coffee_logo

# pprint(MENU)
# pprint(resources)
print(coffee_logo)
resources['money'] = 0

units = {
    "water": "ml",
    "milk": "ml",
    "coffee": "g",
    "money": "$"

}


def report(resource):
    """
    Provides us the Available resource.
    :param resource:
    :return:
    """
    for a in resource:
        if a != "money":
            print(f"{a.title()}:{resource[a]}{units[a]}")
        if a == "money":
            print(f"{a.title()}:{units[a]}{resource[a]} ")


def sufficient_resource_check(user_input):
    """
    Checks whether the available resources are enough for Customer request
    :param user_input:
    :return:
    """
    resource_needed = MENU[user_input]['ingredients']
    for a in resource_needed:
        if resources[a] > resource_needed[a]:
            return True
        else:
            print(f'Sorry there is not enough {a}')
            return False


sufficient_resource_check("latte")


def deduct_resource(user_input):
    """
    Deduct the resource after Completing Customer's Order
    :param user_input:
    :return:
    """
    resource_needed = MENU[user_input]['ingredients']
    for a in resource_needed:
        resources[a] = resources[a] - resource_needed[a]


def userInput():
    """
    This is a virtual coffee Machine that take input from Employee and Customers.
    :return:
    """
    machine_on = True
    while machine_on:
        user_input = input("What would you like? (espresso/latte/cappuccino):").lower()
        if user_input == "off":
            machine_on = False
        elif user_input == "report":
            report(resources)
        elif user_input in MENU:
            # check available resources in Machine are enough to make Latte
            # If not then print "Sorry there is Not enough {resource Name}
            if sufficient_resource_check(user_input) and insert_coins(user_input):
                # Deduct the available resource once the coins inserted are more than enough
                deduct_resource(user_input)
                print(f"Enjoy your {user_input}")
            else:
                userInput()


def insert_coins(user_input):
    """
    Customer enter coins here to process his request.
    Machine tells us whether its enough and refunds them change if they pay more.

    :param user_input:
    :return:
    """
    cost = MENU[user_input]["cost"]
    quarters = int(input("How many Quarters?:"))
    dimes = int(input("How many dimes?:"))
    nickels = int(input("How many nickels?:"))
    pennies = int(input("How many pennies?:"))

    total_paid = 0.25 * quarters + 0.10 * dimes + 0.05 * nickels + 0.01 * pennies

    if total_paid > cost:
        change = total_paid - cost
        if change >= 2.5:
            tip = 2.5
        elif 0 < change < 2.5:
            tip = change
        print(f"Here is your {user_input} and ${round(change - tip, 2)} change.")
        resources['money'] = resources['money'] + tip
        return True
    elif total_paid == cost:
        print(f"Here is your {user_input}. Enjoy your evening Kind Sir")
        return True
    else:
        print(f"Sorry {user_input} costs ${cost},Please enter coins in this Machine Accordingly")
        return False


userInput()
