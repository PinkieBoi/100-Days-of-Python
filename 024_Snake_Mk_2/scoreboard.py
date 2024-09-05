from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.pencolor("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        with open("high_score.txt", "r", encoding="utf-8") as f:
            high_score = f.read()
        self.high_score = int(high_score)
        self.score = 0

    def display_score(self):
        self.clear()
        self.write(f"Score: {self.score}\tHigh Score: {self.high_score}", align="center", font=("Ubuntu", 10, "normal"))

    def increase_score(self):
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=("Ubuntu", 10, "normal"))

    def reset_sb(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", "w", encoding="utf-8") as f:
                f.write(f"{self.high_score}")
        self.score = 0
        self.display_score()
