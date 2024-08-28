import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

win = Screen()
win.setup(600, 600)
win.bgcolor("black")
win.title("Snake Game")
win.tracer(0)
win.listen()

snake = Snake()
food = Food()
scoreboard = Scoreboard()

win.onkeypress(snake.turn_north, "Up")
win.onkeypress(snake.turn_south, "Down")
win.onkeypress(snake.turn_east, "Right")
win.onkeypress(snake.turn_west, "Left")

while snake.game_on:
    win.update()
    time.sleep(0.1)
    scoreboard.display_score(snake.body)
    snake.move_forward()

    # Detect food eaten
    if snake.head.distance(food) < 10:
        food.spawn_food(snake.body)
        snake.add_segment()

if not snake.game_on:
    scoreboard.game_over()

win.exitonclick()
