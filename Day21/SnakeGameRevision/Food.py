import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super(Food, self).__init__()
        self.shape("circle")
        self.color("yellow")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()

    def refresh(self):
        self.goto(random.randint(-270, 270), random.randint(-270, 270))
