from turtle import Screen
from Score import Scoreboard
from Player import Player
from Ball import Ball

canvas = Screen()
canvas.bgcolor("black")
canvas.title("Pong")
canvas.tracer(0)

# canvas.setup(width=1.0, height=1.0)
canvas.screensize(600, 600)
scoreboard = Scoreboard()
# scoreboard.boundary()
scoreboard.scoreLine()

Mic = Player((-300, 0))
Leo = Player((300, 0))
ball = Ball()

canvas.listen()
canvas.onkey(fun=Mic.move_up, key="w")
canvas.onkey(fun=Leo.move_up, key="Up")
canvas.onkey(fun=Mic.move_down, key="s")
canvas.onkey(fun=Leo.move_down, key="Down")

game_on = True
while game_on:
    canvas.update()
    ball.ball_move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.collision()

    if (ball.distance(Leo) < 30 or ball.distance(Mic) < 30) and (ball.xcor() > 300 or ball.xcor() > -300):
        ball.Collision_with_Pad()
        print("Made Contact")

    if ball.xcor() > 300:
        ball.reset_position()
        scoreboard.l_point()
        scoreboard.CurrentScore()

    if ball.xcor() < -300:
        ball.reset_position()
        scoreboard.r_point()
        scoreboard.CurrentScore()

canvas.exitonclick()
