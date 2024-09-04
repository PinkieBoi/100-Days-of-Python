from turtle import Turtle


class PlayerToken(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.goto(0, -280)
        self.seth(90)

    def move_up(self):
        self.fd(10)

    def move_down(self):
        self.bk(10)

    def reset_token(self):
        self.goto(0, -280)
