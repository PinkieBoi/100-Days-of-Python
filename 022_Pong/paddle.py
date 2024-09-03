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
        # self.paddle = []
        # self.limit = location
        # for _ in range(0, 4):
        #     block = Turtle("square")
        #     block.penup()
        #     block.seth(90)
        #     block.color("white")
        #     block.sety(80 - len(self.paddle * 20))
        #     block.setx(self.limit)
        #     self.paddle.append(block)

    def move_up(self):
        self.fd(20)
        # for i in self.paddle:
        #     i.fd(20)

    def move_down(self):
        self.bk(20)
        # for i in self.paddle:
        #     i.bk(20)
