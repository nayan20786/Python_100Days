from turtle import Turtle


class Snake:
    def __init__(self):
        self.positions = [(0, 0), (-20, 0), (-40, 0)]
        self.segments = []
        self.init_snake()

    def init_snake(self):
        """
        initialize the snake length
        This Method will be run Everytime the Snake is Created

        :return:
        """
        for position in self.positions:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.pu()
            new_segment.goto(position)
            self.segments.append(new_segment)
        return self.segments

    def move(self):
        for snake in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[snake - 1].xcor()
            new_y = self.segments[snake - 1].ycor()
            self.segments[snake].goto(new_x, new_y)
        self.segments[0].forward(20)

    def turn_left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)
        # if self.segments[0].xcor() > 0:
        #     self.segments[0].left(90)
        # else:
        #     self.segments[0].right(90)

    def turn_right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)
        # if self.segments[0].xcor() > 0:
        #     self.segments[0].right(90)
        # else:
        #     self.segments[0].left(90)

    def turn_up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def turn_down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def add_segment(self):
        new_segment = Turtle()
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()

        self.segments.append(new_segment)
        pass

    def extend_segment(self):
        x = self.segments[len(self.segments) - 1].xcor()
        y = self.segments[len(self.segments) - 1].ycor()
        self.add_segment()
        self.segments[-1].goto(x, y)
        pass
