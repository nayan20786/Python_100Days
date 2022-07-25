import time
from turtle import Screen, Turtle
from Scorecard import Scorecard
from Snake import Snake
from Food import Food

canvas = Screen()
canvas.bgcolor("black")
canvas.screensize(600, 600)
canvas.tracer(0)

Boundary = Turtle()
Boundary.penup()
Boundary.goto(300, -300)
Boundary.pd()
Boundary.color("white")
Boundary.hideturtle()

for a in range(4):
    Boundary.left(90)
    Boundary.forward(600)
canvas.update()
canvas.listen()

scorecard = Scorecard()
snake = Snake()
food = Food()

canvas.onkeypress(fun=snake.turn_up, key="Up")
canvas.onkeypress(fun=snake.turn_down, key="Down")
canvas.onkeypress(fun=snake.turn_left, key="Left")
canvas.onkeypress(fun=snake.turn_right, key="Right")

game_on = True

while game_on:
    canvas.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food, 1) < 15:
        food.refresh()
        scorecard.increase_score()
        snake.extend_snake()

    if snake.head.xcor() > 300 or snake.head.ycor() < -300 or snake.head.xcor() < -300 or snake.head.ycor() > 300:
        scorecard.game_over()
        game_on = False

    for segment in snake.segments[1::]:
        if snake.head.distance(segment, 1) < 10:
            scorecard.game_over()
            game_on = False

canvas.exitonclick()
