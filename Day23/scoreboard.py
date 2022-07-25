from turtle import Turtle

FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, 290)
        self.score = 0
        self.write(f"SCORE : {self.score}", align="center", font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"SCORE : {self.score}", align="center", font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

    def boundary(self):
        self.penup()
        self.goto(300, -300)
        self.pd()
        for a in range(4):
            self.left(90)
            self.forward(600)
