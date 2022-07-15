# Day8
import math
from datetime import datetime
from art import logo

# Caesar Cypher Project

# 1
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(plain_text, shift_amount):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    K = []
    if direction == "encode":
        for letter in plain_text:
            L = alphabet.index(letter) + shift_amount
            K.append(alphabet[L])

    elif direction == "decode":
        for letter in plain_text:
            L = alphabet.index(letter) - shift_amount
            K.append(alphabet[L])

    cipher_text = "".join(K)
    print(cipher_text)


codeAgain = True

while codeAgain:
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    while shift > 26:
        shift = shift - 26
    while shift < -26:
        shift = shift + 26
    caesar(plain_text=text, shift_amount=shift)
    codeAgain = bool(input("Do you want to code again, True or False"))
exit()


# Prime Number Checker
def PNchecker(number):
    count = 0
    for a in range(1, number + 1):
        if number % a == 0:
            count += 1
        else:
            pass

    if count > 2:
        print("Not a Prime Number")
    else:
        print("Its a Prime Number")


PNchecker(8)
exit()


# Paint area calculator
# Write your code below this line 👇

def paint_calc(height, width, cover):
    total_can_required = math.ceil((height * width) / cover)
    # here i use math.ciel instead of normal round to specifically round it up to upper limit
    print(total_can_required)


# Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

exit()


# greet function with two arguments

def greet(name, location):
    print(f"Hello {name}")
    print(datetime.now())
    print("Code daily to improve")
    print(f"Its raining in {location}")


# calling greet function with Positional Arguments
greet("Nayan", "Bangalore")
# Calling greet function with keyword arguments
greet(location="Jabalpur", name="Nayan")
# here when we use keyword argument order of the character does not matter


exit()


# greet funtion with input
def greet(name):
    print(f"Hello {name}")
    print(datetime.now())
    print("Code daily to improve")


greet("Nayan")

exit()


def greet():
    print("Hi Nayan")
    print(datetime.now())
    print("Code daily to Improve")


greet()
