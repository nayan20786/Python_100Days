from turtle import Turtle


class Player(Turtle):
    def __init__(self, starting_position):
        super(Player, self).__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(starting_position)

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + 80)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - 80)
