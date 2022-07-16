# Day5: Python Loops

import random

# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ""
for a in range(nr_letters):
    password += random.choice(letters)
for a in range(nr_symbols):
    password += random.choice(symbols)
for a in range(nr_numbers):
    password += random.choice(numbers)

L = list(password)
print(L)
random.shuffle(L)
print(L)

print("Normal Password ",password)
# Shuffled Password
password = "".join(L)
print("Shuffled password ",password)

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P


exit()
# FizzBuzz
# You are going to write a program that automatically prints the solution to the FizzBuzz game.
# Your program should print each number from 1 to 100 in turn.
# When the number is divisible by 3 then instead of printing the number it should print "Fizz".
# `When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
# `And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"`

for a in range(1, 101):
    if a % 3 == 0 and a % 5 == 0:
        print("FizzBuzz")
    elif a % 3 == 0:
        print("Fizz")
    elif a % 5 == 0:
        print("Buzz")
    else:
        pass

exit()
# Adding Even Numbers
# You are going to write a program that calculates the sum of all the even numbers from 1 to 100.
# Thus, the first even number would be 2 and the last one is 100
# i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100
total_sum = 0
for a in range(101):
    if a % 2 == 0:
        total_sum = total_sum + a

print(total_sum)
exit()
# High Score Scenario

# You are going to write a program that calculates the highest score from a List of scores.
# e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
# Important you are not allowed to use the max or min functions. The output words must match the example. i.e
# The highest score in the class is: x

student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

max_score = 0

for a in student_scores:
    if max_score < a:
        max_score = a
    else:
        pass

print(max_score)

# Average Student Height Scenario
# You are going to write a program that calculates the average student height from a List of heights.
# e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]
# The average height can be calculated by adding all the heights together and
# dividing by the total number of heights.
# 180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146
# There are a total of 7 heights in student_heights
# 1146 ÷ 7 = 163.71428571428572
# Average height rounded to the nearest whole number = 164
# Important You should not use the sum() or len() functions in your answer.
# You should try to replicate their functionality using what you have learnt about for loops.

student_heights = input("Input a list of student heights ").split()
# converting the student_heights from str to int using loops
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

total_sum = 0
total_students = 0

for n in student_heights:
    total_sum += n
    total_students += 1

print(total_sum)

average_height = total_sum / total_students
print(f"The average height is {round(average_height)}")
exit()
# Some examples

# If we give range 5 it prints till 4,as outer range is not inclusive
for i in range(5):
    print(i)

SAM = [1, 2, 3, 4, 5, 6, 7, 8]

# using 4 loop on list
for a in SAM:
    print(a)
