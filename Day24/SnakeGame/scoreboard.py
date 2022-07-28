from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 16, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.color("white")
        self.penup()
        self.goto(0, 290)
        self.score = 0
        self.highScore = 0
        self.write(f"Score:{self.score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        with open("High_Score.txt", "r") as file:
            self.highScore=int(file.read())
            self.write(f"Score:{self.score} High Score:{self.highScore}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"Game Over", align=ALIGNMENT, font=FONT)

    def high_score(self):
        if self.score >= self.highScore:
            self.highScore = self.score
            with open("High_Score.txt", mode="w") as file:
                file.write(f"{self.highScore}")
        self.score = 0
        self.update_scoreboard()
