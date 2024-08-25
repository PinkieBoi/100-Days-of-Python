import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(500, 400)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
start = [-220, 150]

for color in colors:
    new_turtle = Turtle("turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.setposition(start[0], start[1])
    start[1] -= 60
    turtles.append(new_turtle)
user_guess = screen.textinput("Pick a winner", "Which color turtle will win?")

racing = True
while racing:
    for turtle in turtles:
        turtle.fd(random.randint(1, 10))
        if turtle.xcor() >= 220:
            racing = False
            if user_guess == turtle.fillcolor():
                print(f"You've won. The {turtle.fillcolor()} turtle won the race!")
            else:
                print(f"You've lost. The {turtle.fillcolor()} turtle won the race!")

screen.exitonclick()
