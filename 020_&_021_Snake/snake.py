from turtle import Turtle


class Snake:

    def __init__(self):
        self.game_on = True
        self.body = []
        for _ in range(0, 3):
            self.add_segment()
        for seg in self.body:
            seg.setx(-(self.body.index(seg) * 10))
        self.head = self.body[0]

    def add_segment(self):
        new_segment = Turtle("square")
        new_segment.resizemode("user")
        new_segment.shapesize(0.5, 0.5)
        new_segment.penup()
        new_segment.color("white")
        if len(self.body) >= 3:
            new_segment.goto(self.body[-1].pos())
            new_segment.seth(self.body[-1].heading())
        self.body.append(new_segment)

    def detect_collision_tail(self):
        for s in range(3, len(self.body) - 1):
            if self.head.distance(self.body[s]) < 5:
                self.game_on = False

    def detect_collision_wall(self):
        limit = -300
        if self.head.ycor() >= 250:
            self.game_on = False
        for _ in self.head.pos():
            if _ == limit or _ == abs(limit):
                self.game_on = False

    def move_forward(self):
        for i in range(len(self.body) - 1, 0, -1):
            new_x = self.body[i - 1].xcor()
            new_y = self.body[i - 1].ycor()
            self.body[i].goto(new_x, new_y)
        self.head.fd(10)
        self.detect_collision_wall()
        self.detect_collision_tail()

    def turn_east(self):
        if self.body[1].xcor() != self.head.xcor() + 10:
            self.head.seth(0)

    def turn_north(self):
        if self.body[1].ycor() != self.head.ycor() + 10:
            self.head.seth(90)

    def turn_west(self):
        if self.body[1].xcor() != self.head.xcor() - 10:
            self.head.seth(180)

    def turn_south(self):
        if self.body[1].ycor() != self.head.ycor() - 10:
            self.head.seth(270)
