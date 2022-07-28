import time
from turtle import Turtle, Screen
from Snake import Snake
from Food import Food
from scoreboard import Scoreboard

# Boundary=Turtle()
# Boundary.penup()
# Boundary.goto(300,-300)
# Boundary.pd()
# Boundary.color("white")
# for a in range(4):
#     Boundary.left(90)
#     Boundary.forward(600)


canvas = Screen()
canvas.screensize(600, 600)
canvas.bgcolor("black")
canvas.title("Snake Game")
canvas.tracer(0)

BadGuy = Snake()
food = Food()
canvas.listen()
scoreboard = Scoreboard()
canvas.onkeypress(fun=BadGuy.turn_up, key="Up")
canvas.onkeypress(fun=BadGuy.turn_left, key="Left")
canvas.onkeypress(fun=BadGuy.turn_right, key="Right")
canvas.onkeypress(fun=BadGuy.turn_down, key="Down")

score = 0
game_on = True
while game_on:
    canvas.update()
    time.sleep(0.1)
    BadGuy.move()

    if BadGuy.segments[0].distance(food, 1) < 15:
        food.refresh()
        score += 1
        scoreboard.increase_score()
        BadGuy.extend_segment()

    #     Detect Collision with Wall
    if BadGuy.segments[0].xcor() > 300 or BadGuy.segments[0].xcor() < -300 or BadGuy.segments[0].ycor() > 300 or \
            BadGuy.segments[0].ycor() < -300:
        BadGuy.reset_segments()
        scoreboard.high_score()
        # game_on = False
        # scoreboard.game_over()

    # Detect Collision with Tail
    for a in BadGuy.segments[1::]:
        if BadGuy.segments[0].distance(a, 1) < 10:
            BadGuy.reset_segments()
            scoreboard.high_score()
            # game_on = False
            # scoreboard.game_over()

canvas.exitonclick()

# positions = [(0, 0), (-20, 0), (-40, 0)]
# segments = []
# for position in positions:
#     new_segment = Turtle(shape="square")
#     new_segment.color("white")
#     new_segment.pu()
#     new_segment.goto(position)
#     segments.append(new_segment)
#
# # snake.shapesize(1,3,3))
# game_on = True
# while game_on:
#     canvas.update()
#     time.sleep(1)
#     for snake in range(len(segments) - 1, 0, -1):
#         new_x = segments[snake - 1].xcor()
#         new_y = segments[snake - 1].ycor()
#         segments[snake].goto(new_x, new_y)
# segments[0].forward(20)
# segments[0].left(90)
