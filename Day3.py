import math

# Treasure Island Code

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

move1 = input("Where do you wanna go Left or Right??")

if move1 == "Left":
    move2 = input("Do you want to swim or wait")
    if move2 == "wait":
        door = input("Which door will you choose_ Red,Blue,Yellow")
        if door == "Yellow":
            print("You win")
        elif door == "Red":
            print("You got burned by fire")
        elif door == "Blue":
            print("Eaten by Beasts")
        else:
            print("Cant even choose correct options looser")
    else:
        print("You dies lmfao")
else:
    print("You Died Lmao")

exit()
# Love Calculator
# We can count the occurrence of a value in strings using the count() function.
# It will return how many times the value appears in the given string.
# For Love Scores less than 10 or greater than 90, the message should be:
# "Your score is **x**, you go together like coke and mentos."
# For Love Scores between 40 and 50, the message should be:
# "Your score is **y**, you are alright together."
# Otherwise, the message will just be their score. e.g.:
# "Your score is **z**."

name1 = input("Enter Name 1")
name2 = input("Enter Name 2")

# TRUE
TRUE = name1.count('T') + name1.count('R') + name1.count('U') + name1.count('E') + \
       name1.count('t') + name1.count('r') + name1.count('u') + name1.count('e')
LOVE = name2.count('L') + name2.count('0') + name2.count('V') + name2.count('E') \
       + name2.count('l') + name2.count('o') + name2.count('v') + name2.count('e')

True_Love = int(f"{TRUE}{LOVE}")

if True_Love > 90 or True_Love < 10:
    print(f"Your score is **{True_Love}**, you go together like coke and mentos.")
elif 40 < True_Love < 50:
    print(f"Your score is **{True_Love}**, you are alright together.")
else:
    print(f"Your score is **{True_Love}**.")

exit()
# Leap Year Scenario

year = int(input("Enter the value of year you want to find out is leap or Not"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year")
        else:
            print("Not Leap Year")
    else:
        print("Leap Year")
else:
    print("Not leap year")

exit()
# Ride fare Scenario
height = int(input("What is your Height?:: "))
age = int(input("What is your age?:: "))

want_photos = bool(input("Do you want Photos::True or False"))
if want_photos:
    fare = 3
else:
    fare = 0

# Ticketing System
if height > 120:
    print("You full-fill one  eligibility criteria for the ride")
    if age < 12:
        fare += 5
        print(f"${fare}")
    elif 12 < age < 18:
        fare += 7
        print(f"${fare}")
    elif age > 18:
        if 45 < age < 55:
            print("Enjoy your ride for free")
        else:
            fare += 12
            print(f"${fare}")
else:
    print("Sorry you are not Eligible for this ride")

exit()
# BMI 2.0
# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
#
# It should tell them the interpretation of their BMI based on the BMI value.
#
# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.

weight = float(input("Enter the value of your weight in KG"))
height = float(input("Enter the value of your Height in METER"))

BMI = int(weight / (math.pow(height, 2)))
print(BMI)

if BMI > 35:
    print(f"BMI::{BMI}::You are clinically obese")
elif 35 > BMI > 30:
    print(f"BMI::{BMI}::obese")
elif 30 > BMI > 25:
    print(f"BMI::{BMI}::Slightly Overweight")
elif 25 > BMI > 20:
    print(f"BMI::{BMI}::normal weight")
elif BMI < 20:
    print(f"BMI::{BMI}::underweight")
else:
    print("Invalid input")
exit()
# Odd/Even Program
number = int(input("Which number do you want to check? "))

if number % 2 == 0:
    print("The number is Even")
else:
    print("The number is ODD")
