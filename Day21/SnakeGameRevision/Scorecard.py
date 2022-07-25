from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 14, 'normal')


class Scorecard(Turtle):
    def __init__(self):
        super(Scorecard, self).__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 301)
        self.pd()
        self.write(f"SCORE:{self.score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"SCORE:{self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"SCORE:{self.score}", align=ALIGNMENT, font=FONT)
