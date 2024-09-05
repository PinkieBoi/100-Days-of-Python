import time
from turtle import Screen
from cars import CarManager
from player import PlayerToken
from scoreboard import Scoreboard

win = Screen()
win.bgcolor("black")
win.setup(width=600, height=600)
win.tracer(0)
win.listen()

score = Scoreboard()
player = PlayerToken()
cars = CarManager()

win.onkeypress(player.move_up, "Up")
win.onkeypress(player.move_down, "Down")

game_on = True
while game_on:
    win.update()
    time.sleep(0.1)
    score.display_level()
    cars.move_cars(score.level)

    # Loop cars
    for car in cars.all_cars:
        if car.xcor() <= -320:
            car.setx(320)

    # Detect Game Over
    for car in cars.all_cars:
        if player.distance(car) <= 20 or player.xcor() == car.xcor() and player.distance(car) <= 20:
            score.game_over()
            game_on = False

    # Level Complete
    if player.ycor() >= 280:
        player.reset_token()
        score.level += 1
        cars.add_cars(5)

win.exitonclick()
