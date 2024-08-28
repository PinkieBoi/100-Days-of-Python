import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.color("blue")
        self.shape("circle")
        self.speed("fastest")
        self.resizemode("user")
        self.shapesize(0.5)
        self.penup()
        self.goto(random.randint(-280, 280), random.randint(-280, 280))

    def spawn_food(self, body):
        point = (random.randint(-280, 280), random.randint(-280, 280))
        for _ in body:
            if point[0] in range(int(_.pos()[0]) - 6, int(_.pos()[0] + 6)):
                point = (random.randint(-280, 280), random.randint(-280, 280))
            elif point[1] in range(int(_.pos()[1]) - 6, int(_.pos()[1] + 6)):
                point = (random.randint(-280, 280), random.randint(-280, 280))
        self.goto(point)
