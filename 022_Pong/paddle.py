from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, location):
        super().__init__()
        self.penup()
        self.seth(90)
        self.color("white")
        self.setx(location)
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=4)

    def move_up(self):
        self.fd(20)

    def move_down(self):
        self.bk(20)
