from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score1 = 0
        self.score2 = 0
        self.pensize(10)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.game_on = True

    def display_score(self, limit):
        self.clear()
        self.goto(0, limit - 50)
        self.write(f"{self.score1}\t{self.score2}", align="center", font=("Roboto", 20, "normal"))


class GameBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.seth(270)
        self.goto(0, 350)
        while self.ycor() > -350:
            self.fd(20)
            self.pendown()
            self.fd(20)
            self.penup()
