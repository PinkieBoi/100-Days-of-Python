from turtle import Turtle

FONT = ("Ubuntu", 10, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(-250, 250)
        self.level = 1

    def display_level(self):
        self.clear()
        self.write(arg=f"Level:  {self.level}", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=FONT)
