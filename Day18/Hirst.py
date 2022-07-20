import turtle
import random
# import colorgram
from turtle import Turtle, Screen
from pprint import pprint

timmy = Turtle()
turtle.colormode(255)
turtle.speed(100)
timmy.pensize(30)
canvas = Screen()

# colors = colorgram.extract("hirst_dots.jpg", 50)
#
# # pprint(colors)
# print(len(colors))
#
# k = []
#
#
# def color_ra():
#     for a in range(0, len(colors) - 1):
#         r = colors[a].rgb.r
#         g = colors[a].rgb.g
#         b = colors[a].rgb.b
#         random_color = (r, g, b)
#         k.append(random_color)
#     return k
# print(color_ra())
canvas.screensize(canvwidth=1920, canvheight=1080)
rgb_colors = [(249, 246, 242), (239, 245, 249), (250, 243, 247), (244, 250, 247), (139, 164, 183), (26, 116, 172),
              (238, 213, 64), (202, 140, 166), (222, 158, 82), (121, 71, 96), (24, 135, 63), (137, 22, 37),
              (70, 31, 37), (182, 176, 32), (185, 76, 41), (224, 171, 197), (55, 36, 34), (30, 169, 182), (230, 87, 39),
              (107, 191, 135), (11, 108, 66), (46, 171, 89), (183, 95, 110), (38, 37, 43), (188, 183, 209),
              (157, 208, 214), (151, 214, 172), (237, 172, 154), (126, 116, 156), (79, 55, 54), (12, 102, 105),
              (200, 210, 35), (65, 58, 79)]
# Once you have extracted the colors comment out that code

for a in range(11):
    for b in range(11):
        timmy.dot(20, random.choice(rgb_colors))
        timmy.pu()
        timmy.forward(50)
        timmy.pd()

    timmy.pu()
    timmy.setpos(0, 0)
    timmy.position()
    timmy.left(90)
    timmy.forward(50 * a)
    timmy.right(90)
    timmy.pd()

canvas.exitonclick()
