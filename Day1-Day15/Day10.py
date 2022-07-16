# Day10
# Calculator
from art import calculator_logo

print(calculator_logo)


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiple(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    '+': add,
    '-': subtract,
    '*': multiple,
    '/': divide
}


def calculator():
    num1 = float(input("Whats the first Number ?"))
    for operation in operations:
        print(operation)
    should_continue = True
    while should_continue:
        operation_symbol = input("Pick as operation from the line above")
        num2 = float(input("Whats the Second Number ?"))
        calculate_function = operations[operation_symbol]
        answer = calculate_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()

exit()


# Function with Outputs
def is_leap(input_year):
    """
    Function to calculate whether the input year is leap or not
    :param input_year:
    :return:
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(input_year, input_month):
    if is_leap(input_year):
        month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return month_days[input_month - 1]
    else:
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return month_days[input_month - 1]


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

exit()


# Title Case Creator
def titleCaseCreator():
    f_name = input("Enter first name")
    l_name = input("Enter last name")

    return f_name.title() + " " + l_name.title()


FullName = titleCaseCreator()
print(FullName)
