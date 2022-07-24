import time
from turtle import Turtle, Screen
from Snake import Snake

canvas = Screen()
canvas.screensize(600, 600)
canvas.bgcolor("black")
canvas.title("Snake Game")
canvas.tracer(0)

BadGuy = Snake()
canvas.listen()

canvas.onkeypress(fun=BadGuy.turn_up, key="Up")
canvas.onkeypress(fun=BadGuy.turn_left, key="Left")
canvas.onkeypress(fun=BadGuy.turn_right, key="Right")
canvas.onkeypress(fun=BadGuy.turn_down, key="Down")

game_on = True
while game_on:
    canvas.update()
    time.sleep(0.1)
    BadGuy.move()

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
