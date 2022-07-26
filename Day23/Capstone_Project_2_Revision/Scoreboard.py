from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.penup()
        self.goto(-250, 250)
        self.color("red")
        self.score = 0
        self.pd()
        self.write(f"SCORE:{self.score}", align="left", font=('Arial', 20, 'bold'))
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"SCORE:{self.score}", align="left", font=('Arial', 20, 'bold'))

    def game_over(self):
        self.clear()
        self.penup()
        self.goto(0, 0)
        self.pendown()
        self.color("black")
        self.write(f"GAME OVER", align="center", font=('Arial', 20, 'bold'))
