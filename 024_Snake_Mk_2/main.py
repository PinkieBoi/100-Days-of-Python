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

game_on = True
while game_on:
    win.update()
    time.sleep(0.1)
    scoreboard.display_score()
    snake.move_forward()

    # Detect food eaten
    if snake.head.distance(food) < 10:
        food.spawn_food(snake.body)
        scoreboard.increase_score()
        snake.add_segment()

    # Detect collision with tail
    for s in snake.body[3:]:
        if snake.head.distance(s) < 5:
            scoreboard.reset_sb()
            snake.reset_snake()

    # Detect collision with wall
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        scoreboard.reset_sb()
        snake.reset_snake()

win.exitonclick()
