# Day 19

# Challenge 1:Etch a Sketch
import turtle
from turtle import Turtle, Screen

turtle.pensize(40)
tim = Turtle()
canvas = Screen()
turtle.speed(300)

tim.shape("turtle")
tim.shapesize(5)


def move_forword():
    tim.forward(10)


def move_backword():
    tim.back(10)


def turn_right():
    tim.right(10)


def turn_left():
    tim.left(10)


def clsTurtle():
    tim.reset()


canvas.listen()
canvas.onkey(fun=move_forword, key="w")
canvas.onkey(fun=move_backword, key="s")
canvas.onkey(fun=clsTurtle, key="space")
canvas.onkey(fun=turn_left, key="d")
canvas.onkey(fun=turn_right, key="a")
canvas.exitonclick()
