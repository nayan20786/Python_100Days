import turtle
from turtle import Turtle

turtle.register_shape("Leo80.gif")
turtle.register_shape("Turtles.gif")


class Player(Turtle):
    def __init__(self):
        super(Player, self).__init__()
        self.shape("Leo80.gif")
        self.penup()
        self.setheading(90)
        self.goto(0, -250)

    def move(self):
        self.forward(30)

    def reset_position(self):
        self.goto(0, -250)

    # def change_shape(self):
    #     self.shape("Turtles.gif")

