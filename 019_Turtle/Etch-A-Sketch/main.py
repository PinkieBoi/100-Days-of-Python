from turtle import Turtle, Screen


def turn_left():
    t.left(10)


def turn_right():
    t.right(10)


def move_forward():
    t.fd(10)


def move_backwards():
    t.bk(10)


def move_left():
    turn_left()
    move_forward()


def move_right():
    turn_right()
    move_forward()


def clear_drawing():
    t.clear()
    t.penup()
    t.home()
    t.pendown()


t = Turtle()
screen = Screen()
screen.listen()


screen.onkeypress(move_forward, "w")
screen.onkeypress(turn_left, "a")
screen.onkeypress(move_backwards, "s")
screen.onkeypress(turn_right, "d")
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")
screen.onkeypress(clear_drawing, "c")

screen.exitonclick()
