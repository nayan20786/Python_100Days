import random
import time
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super(Ball, self).__init__()
        self.shape("circle")
        self.color("white")
        # self.penup()
        self.shapesize(stretch_wid=2, stretch_len=2)
        self.move_x = 0.4
        self.move_y = 0.4
        # self.angle = random.randint(0, 360)

    def ball_move(self):
        x = self.xcor() + self.move_x
        y = self.ycor() + self.move_y
        self.goto(x, y)

    # Adding a Ball Bouncing Logic
    def collision(self):
        self.move_y *= -1
        # self.move_y += 1
        # self.move_x += 1

    # Detect Collision with Player
    def Collision_with_Pad(self):
        self.move_x *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.Collision_with_Pad()
