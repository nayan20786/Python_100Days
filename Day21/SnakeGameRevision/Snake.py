from turtle import Turtle


class Snake(Turtle):
    def __init__(self):
        super(Snake, self).__init__()
        self.segments = []
        self.position = [(0, 0), (-20, 0), (-40, 0)]
        self.init_snake()
        self.head = self.segments[0]

    def init_snake(self):
        for position in self.position:
            new_segment = Turtle()
            new_segment.shape("square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(position)
            self.segments.append(new_segment)

    def add_segment(self):
        new_segment = Turtle()
        new_segment.shape("square")
        new_segment.penup()
        new_segment.color("white")
        self.segments.append(new_segment)

    def extend_snake(self):
        # x = self.segments[-1].xcor()
        # y = self.segments[-1].ycor()
        position = self.segments[-1].position()
        self.add_segment()
        # self.segments[-1].goto(x, y)
        self.segments[-1].goto(position)

    def move(self):
        for snake in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[snake - 1].xcor()
            new_y = self.segments[snake - 1].ycor()
            self.segments[snake].goto(new_x, new_y)
        self.head.forward(20)

    def turn_left(self):
        if self.head.heading() != 0:
            self.segments[0].setheading(180)

    def turn_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def turn_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def turn_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
