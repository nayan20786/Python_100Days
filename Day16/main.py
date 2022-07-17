from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from Day1_Day15.art import coffee_logo

print(coffee_logo)
coffee_machine = Menu()
coffee_machine_rep = CoffeeMaker()
coffee_machine_money = MoneyMachine()


# coffee_machine_Item = MenuItem(drink,water,milk,coffee,cost)

def userInput():
    """
    This is a virtual coffee Machine that take input from Employee and Customers.
    :return:
    """
    machine_on = True
    while machine_on:
        order_name = input("What would you like? " + coffee_machine.get_items().lower())
        if order_name == "off":
            machine_on = False
        elif order_name == "report":
            print("********************")
            coffee_machine_rep.report()
            print("********************")
            coffee_machine_money.report()
            print("********************")
        else:
            drink = coffee_machine.find_drink(order_name)
            cost = coffee_machine.find_drink(order_name).cost
            if coffee_machine_rep.is_resource_sufficient(drink) and coffee_machine_money.make_payment(
                    cost):
                coffee_machine_rep.make_coffee(drink)
                print(f"Enjoy your {order_name}")



userInput()
