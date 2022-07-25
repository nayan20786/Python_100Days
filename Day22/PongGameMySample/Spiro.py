import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)

timmy = Turtle()
canvas = Screen()

timmy.shape('turtle')
timmy.pensize(15)
turtle.speed(100)


# timmy.speed("fastest")

def randomRGB():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


for a in range(100):
    turtle.circle(100)
    turtle.right(5)
    timmy.color(randomRGB())

canvas.exitonclick()
