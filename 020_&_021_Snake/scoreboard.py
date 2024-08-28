from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.pencolor("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)

    def display_score(self, body):
        score = len(body) - 3
        self.clear()
        self.write(f"Score:\t{score}", align="center", font=("Ubuntu", 10, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=("Ubuntu", 10, "normal"))

