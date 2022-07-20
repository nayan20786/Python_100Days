# I was working on creating a Hirst Painting using colorgram,Turtle
import turtle
from turtle import Turtle, Screen
import colorgram
from pprint import pprint
import random

turtle.colormode(255)
turtle.pensize(5)
turtle.pensize(30)

timmy = Turtle()
canvas = Screen()
turtle.speed(100)
colors = colorgram.extract("hirst_dots.jpg", 100)
print(len(colors))

print(colors[3].rgb)
canvas.screensize(2000)


def randomRGB():
    a = random.randint(0, int(len(colors)) - 1)
    print(a)
    r = colors[a].rgb.r
    g = colors[a].rgb.g
    b = colors[a].rgb.b
    random_color = (r, g, b)
    return random_color


# def randomRGB():
for b in range(6):
    if b % 2 != 0:
        timmy.right(90)
        timmy.forward(40)
        timmy.right(90)
    else:

        timmy.forward(40)
        timmy.left(90)

    for a in range(5):
        timmy.fillcolor(randomRGB())
        timmy.begin_fill()
        timmy.circle(10)
        timmy.end_fill()
        timmy.pu()
        timmy.left(90)
        timmy.forward(40)
        timmy.pd()

canvas.exitonclick()
