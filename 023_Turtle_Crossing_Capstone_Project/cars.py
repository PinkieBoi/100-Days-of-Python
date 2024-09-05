import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.add_cars(10)

    def move_cars(self, level):
        speed = STARTING_MOVE_DISTANCE + (MOVE_INCREMENT * (level - 1))
        for car in self.all_cars:
            car.fd(speed)

    def add_cars(self, num_cars):
        for _ in range(num_cars):
            new_car = Turtle("square")
            new_car.penup()
            new_car.seth(180)
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.goto(random.randint(-50, 800), random.randint(-250, 250))
            self.all_cars.append(new_car)

    # def example_create_car(self):
    #     random_chance = random.randint(1, 6)
    #     if random_chance == 1:
    #         new_car = Turtle("square")
    #         new_car.shapesize(stretch_len=2, stretch_wid=1)
    #         new_car.penup()
    #         new_car.color(random.choice(COLORS))
    #         random_y = random.randint(-250, 250)
    #         new_car.goto(300, random_y)
    #         self.all_cars.append(new_car)
