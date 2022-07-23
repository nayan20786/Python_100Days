import turtle
from turtle import Turtle, Screen
import random
from pprint import pprint

turtle.colormode(255)

turtle_colors = ["blue", "red", "green", "yellow", "brown", "violet", "purple", "pink", "orange"]

tim = Turtle(shape="turtle")
canvas = Screen()
tim.pu()
tim.goto(230, -150)
tim.pd()
tim.goto(230, 150)

Turtle_Racers = int(canvas.textinput(title="Number of Turtles", prompt="How many Turtles do you want in the race"))
tim.penup()
tim.goto(-230, 0)
Racers = [tim]
for a in range(1, Turtle_Racers):
    marty = Turtle(shape="turtle")
    marty.color(turtle_colors[a])
    marty.pu()
    if a % 2 == 0:
        a = -1 * a
        marty.goto(-230, a * 20)
    else:
        marty.goto(-230, a * 20)
    Racers.append(marty)

placeBet = canvas.textinput(title="Place Bet", prompt="Which Turtle do you wanna bet money on?: input color").lower()
move = [10, 20, 30, 50, 5, 3, 4, 9]
race_on = True
while race_on:
    for racers in Racers:
        t_move = random.choice(move)
        racers.forward(t_move)
        # print(racers.xcor())

        if racers.xcor() >= 230:
            print(racers.color())
            race_on = False
            if racers.color()[1] == placeBet:
                print("You win")
            else:
                print("You lose")
# canvas.listen()
# canvas.onkey(fun=start_Race, key='w')

pprint(Racers)
canvas.exitonclick()
