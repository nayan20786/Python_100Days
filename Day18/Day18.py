# Day 18
# To execute some code just copy adn paste it in seperate python file then try Executing
import turtle
from turtle import Turtle, Screen
import random
turtle.colormode(255)

timmy = Turtle()
canvas = Screen()


timmy.shape('turtle')
timmy.pensize(15)
timmy.speed("fastest")


def randomRGB():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


# turtle_colors = ["blue", "dark slate blue", "Brown", "dark red", "DarkOrange", "black", "red"]
random_direction = ["timmy.right(90)", "timmy.left(90)"]
# 4th challenge: random walk

for a in range(50):
    eval(random.choice(random_direction))
    timmy.forward(20)
    timmy.color(randomRGB())

canvas.exitonclick()
# 1st Challenge
# timmy.forward(100)

# for a in range(3):
#     timmy.color("blue")
#     timmy.left(90)
#     timmy.color("red")
#     timmy.forward(100)

# 2nd Challenge
# for a in range(50):
#     timmy.forward(1)
#     timmy.pu()
#     timmy.forward(5)
#     timmy.pd()

# 3rd Challenge

# Creating a method
exit()


def drawShape(sides):
    angle = 360 / sides
    for b in range(sides + 1):
        timmy.forward(100)
        timmy.right(angle)
    timmy.color(random.choice(turtle_colors))


drawShape(10)

# Running a simple for loop
for Sides in range(3, 11):
    angle = 360 / Sides
    for b in range(Sides + 1):
        timmy.forward(100)
        timmy.right(angle)
    timmy.color(random.choice(turtle_colors))

# Commented the Long way
# for a in range(3):
#     timmy.forward(100)
#     timmy.right(120)
#
# timmy.color(random.choice(turtle_colors))
#
# for a in range(4):
#     timmy.forward(100)
#     timmy.right(90)
#
# timmy.color(random.choice(turtle_colors))
#
# for a in range(5):
#     timmy.forward(100)
#     timmy.right(180-108)
#
# timmy.color(random.choice(turtle_colors))
#
# for a in range(6):
#     timmy.forward(100)
#     timmy.right(60)
#
# timmy.color(random.choice(turtle_colors))
#
# for a in range(7):
#     timmy.forward(100)
#     timmy.right(180-128.57)
#
# for a in range(8):
#     timmy.forward(100)
#     timmy.right(180 - 135)
#
# for a in range(9):
#     timmy.forward(100)
#     timmy.right(180 - 140)
#
# for a in range(10):
#     timmy.forward(100)
#     timmy.right(180-144)

# timmy.forward(100)
canvas.exitonclick()
