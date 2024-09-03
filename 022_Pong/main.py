import time
from ball import Ball
from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard, GameBoard

win = Screen()
win.setup(width=1000, height=700)
win.title("Pong")
win.bgcolor("black")
win.tracer(0)
win.listen()
board = GameBoard()

r_paddle = Paddle(450)
l_paddle = Paddle(-450)

score = Scoreboard()
score.display_score(win.window_height())
ball = Ball()

win.onkeypress(r_paddle.move_up, "Up")
win.onkeypress(r_paddle.move_down, "Down")
win.onkeypress(l_paddle.move_up, "w")
win.onkeypress(l_paddle.move_down, "s")

while score.score1 + score.score2 != 11:
    ball.reset_ball(score.score1 + score.score2)
    score.display_score(350)
    score.game_on = True
    print(r_paddle.position())
    while score.game_on:
        win.update()
        time.sleep(0.1)
        ball.move_forward(l_paddle, r_paddle)
        if ball.xcor() > 480:
            score.score2 += 1
            score.game_on = False
        if ball.xcor() < -480:
            score.score1 += 1
            score.game_on = False

win.exitonclick()
