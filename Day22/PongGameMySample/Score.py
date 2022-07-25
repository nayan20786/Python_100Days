from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.score_player1 = 0
        self.score_player2 = 0
        self.hideturtle()
        self.boundary()
        self.CurrentScore()

    def boundary(self):
        self.penup()
        self.goto(300, -300)
        self.pendown()

        for a in range(4):
            self.left(90)
            self.forward(600)

    def scoreLine(self):
        self.penup()
        self.goto(0, -300)
        self.left(90)
        self.pensize(5)
        for a in range(8):
            self.pendown()
            self.forward(40)
            self.penup()
            self.forward(40)

    def CurrentScore(self):
        self.clear()
        self.penup()
        self.goto(-200, 200)
        self.write(f"{self.score_player1}", font=("Nova Square", 40, "bold"))
        self.goto(200, 200)
        self.write(f"{self.score_player2}", font=("Nova Square", 40, "bold"))

    def l_point(self):
        self.score_player1 += 1

    def r_point(self):
        self.score_player2 += 1
