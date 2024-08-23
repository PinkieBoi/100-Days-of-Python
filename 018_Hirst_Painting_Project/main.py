import random
from turtle import Turtle, Screen
from catppuccin_colors import colors, background_color


def line_of_grid(num_grid):
    for _ in range(num_grid):
        tommy.pencolor(colors[random.choice(color_list)])
        tommy.dot(25)
        tommy.fd(45)


def painting(grid, start):
    tommy.setx(start)
    y_position = -350
    for _ in range(grid):
        tommy.setx(start)
        tommy.sety(y_position)
        line_of_grid(grid)
        y_position += 45


tommy = Turtle()
tommy.shape("circle")
tommy.speed("fastest")
tommy.penup()
tommy.setx(-400)
tommy.sety(-350)

screen = Screen()
screen.bgcolor(background_color['base'])

tommy.pencolor(colors['flamingo'])
color_list = []
for k in colors:
    color_list.append(k)

painting(17, -400)

screen.exitonclick()
