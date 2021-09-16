from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
paddle = Turtle()
scoreboard = Scoreboard()

screen.bgcolor("black")
screen.setup(width=1000, height=700)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((450, 0))
l_paddle = Paddle((-450, 0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "e")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detect ball collision with wall
    if ball.ycor() > 320 or ball.ycor() < -320:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    if ball.xcor() > 500:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -500:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
