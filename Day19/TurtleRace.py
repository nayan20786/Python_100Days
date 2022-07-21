import turtle
from turtle import Turtle, Screen
from pprint import pprint
import random

tim = Turtle(shape="turtle")
tim.color("Dark Orange")
canvas = Screen()

canvas.setup(width=500, height=400)

numOfTurtles = int(turtle.textinput("players", "How many turtles do you want in the Race"))
print(numOfTurtles)

colors = ["Red", "green", "blue", "yellow", "pink", "purple", "Black", "brown", "dark green"]
Turtle_list = [tim]
tim.penup()
tim.goto(-230, -10)
for a in range(1, numOfTurtles + 1):
    kurt = Turtle(shape="turtle")
    kurt.color(colors[a])
    kurt.penup()
    if a % 2 == 0:
        a = a * (-1)
        kurt.goto(-230, 20 * a)
    else:
        kurt.goto(-230, 20 * a)
    Turtle_list.append(kurt)

move = [10, 20, 30]

canvas.listen()


def Move_forward():
    tim.forward(random.choice(move))


def start_race():
    individual_distance = []
    for marty in Turtle_list:
        j = random.choice(move)
        marty.forward(j)


canvas.onkey(key="w", fun=Move_forward)
canvas.onkey(key="s", fun=start_race)
pprint(Turtle_list)

canvas.exitonclick()
