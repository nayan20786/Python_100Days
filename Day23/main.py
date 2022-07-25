import time, random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

Tim = Player()
scoreboard = Scoreboard()
car = CarManager()
screen.onkeypress(fun=Tim.move_turtle, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_cars()
    car.move_cars()

    if Tim.ycor() == 280:
        Tim.reset_position()
        scoreboard.increase_score()
        car.level_up()

    for a in car.all_cars:
        if a.distance(Tim) < 20:
            game_is_on = False
            scoreboard.game_over()

    for cars in car.all_cars:
        if cars.xcor() < -320:
            car.all_cars.remove(cars)

    # reset turtle position increase score

screen.exitonclick()
