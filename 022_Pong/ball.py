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
        if match_round % 3 == 0 or match_round == 0:
            self.seth(90)
            direction = random.randrange(30, 150)
            self.rt(direction)
            self.fd(50)
        else:
            self.seth(270)
            direction = random.randrange(30, 150)
            self.rt(direction)
            self.fd(50)

    def move_forward(self, left_paddle, right_paddle):
        self.fd(10)
        self.wall_bounce()
        self.paddle_bounce(left_paddle, right_paddle)

    def wall_bounce(self):
        # reflection = random.randint(40, 100)
        if self.ycor() >= 350 or self.ycor() <= -350:
            # if self.heading() == 90 or self.heading() == 270:
            #     if self.ycor() > 0:
            #         pass
            #     else:
            #         pass
            if self.heading() in range(91, 180) or self.heading() in range(271, 360):
                self.lt(90)
                self.fd(10)
                self.fd(10)
            else:
                self.rt(90)
                self.fd(10)
                self.fd(10)

    # def paddle_bounce(self, left_paddle, right_paddle):
    #     if self.xcor() > 0:
    #         for i in right_paddle:
    #             if self.distance(i) <= 15:
    #                 if self.heading() == 0:
    #                     self.rt(random.randint(170, 190))
    #                     self.fd(50)
    #                 elif 0 < self.heading() > 90:
    #                     self.rt(random.randint(45, 90))
    #                     self.fd(50)
    #                 else:
    #                     self.lt(random.randint(45, 90))
    #                     self.fd(50)
    #     else:
    #         for i in left_paddle:
    #             if self.distance(i) <= 15:
    #                 if self.heading() == 180:
    #                     self.rt(random.randint(170, 190))
    #                     self.fd(90)
    #                 elif 90 < self.heading() > 180:
    #                     self.lt(random.randint(45, 90))
    #                     self.fd(90)
    #                 else:
    #                     self.rt(random.randint(45, 90))
    #                     self.fd(90)

    def paddle_bounce(self, left_paddle, right_paddle):
        if self.xcor() < -430:
            if left_paddle.ycor() - 40 <= self.ycor() <= left_paddle.ycor() + 40:
                # if 170 < self.heading() > 190:
                #     self.lt(random.randint(160, 200))
                if 90 < self.heading() > 180:
                    self.lt(90)
                else:
                    self.rt(90)
                self.fd(20)
        if self.xcor() > 430:
            if right_paddle.ycor() - 40 <= self.ycor() <= right_paddle.ycor() + 40:
                # if self.heading() < 20 or self.heading() > 340:
                #     self.rt(random.randint(160, 200))
                if 0 < self.heading() > 90:
                    self.rt(90)
                else:
                    self.lt(90)
                self.fd(20)
