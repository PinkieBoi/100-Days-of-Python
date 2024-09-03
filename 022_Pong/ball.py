import random
from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")

    def reset_ball(self, match_round):
        self.goto(0, 0)
        if match_round % 2 == 0 or match_round == 0:
            self.seth(90)
            direction = random.randrange(30, 150)
            self.rt(direction)
        else:
            self.seth(270)
            direction = random.randrange(30, 150)
            self.rt(direction)

    def move_forward(self, left_paddle, right_paddle):
        self.fd(20)
        self.wall_bounce()
        self.paddle_bounce(left_paddle, right_paddle)

    def wall_bounce(self):
        if self.ycor() >= 350 or self.ycor() <= -350:
            if self.heading() in range(91, 180) or self.heading() in range(271, 360):
                self.lt(90)
                self.fd(20)
            else:
                self.rt(90)
                self.fd(20)

    def paddle_bounce(self, left_paddle, right_paddle):
        if self.xcor() < -430:
            # Could have used if self.distance(right_paddle) < 40 and self.xcor <= -430
            # with an or statement to include distance to left paddle
            if left_paddle.ycor() - 40 <= self.ycor() <= left_paddle.ycor() + 40:
                if 90 < self.heading() > 180:
                    self.lt(random.randint(80, 120))
                else:
                    self.rt(random.randint(80, 120))
                self.fd(20)
        if self.xcor() > 430:
            if right_paddle.ycor() - 40 <= self.ycor() <= right_paddle.ycor() + 40:
                if 0 < self.heading() > 90:
                    self.rt(random.randint(80, 120))
                else:
                    self.lt(random.randint(80, 120))
                self.fd(20)
