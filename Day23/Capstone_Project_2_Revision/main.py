import time
import turtle
from turtle import Screen
from Scoreboard import Scoreboard
from Player import Player
from Car_Manager import Car_Manager

turtle.colormode(255)

screen = Screen()
screen.setup(width=600, height=600)
screen.bgpic("Road3.gif")
screen.tracer(0)

screen.bgcolor((149, 149, 149))

Leo = Player()
Garage = Car_Manager()
scoreboard = Scoreboard()
screen.listen()
screen.onkeypress(fun=Leo.move, key="Up")

game = True
while game:
    time.sleep(0.1)
    screen.update()
    Garage.create_car()
    Garage.car_move()

    for car in Garage.car:
        if car.distance(Leo) < 30:
            # Leo.change_shape()
            scoreboard.game_over()
            game = False
        if car.xcor() < -280:
            del car
    if Leo.ycor() >= 280:
        scoreboard.increase_score()
        Leo.reset_position()
        Garage.increase_car_speed()

screen.exitonclick()
