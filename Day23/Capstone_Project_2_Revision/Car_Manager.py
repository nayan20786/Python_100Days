import random
from turtle import Turtle

COLORS = ["red", "green", "yellow", "blue", "yellow", "purple", "pink", "brown", "black"]
MOVE_SPEED = 5
INCREMENT_SPEED = 10


class Car_Manager:
    def __init__(self):
        self.car = []
        self.speed = MOVE_SPEED

    def create_car(self):
        if random.randint(1, 6) == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.setheading(180)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(280, random.randint(-250, 250))
            self.car.append(new_car)

    def car_move(self):
        for car in self.car:
            car.forward(self.speed)

    def increase_car_speed(self):
        self.speed += INCREMENT_SPEED
