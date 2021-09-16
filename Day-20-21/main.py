from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    # Collision of snake with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    x_cor = snake.head.xcor()
    y_cor = snake.head.ycor()
    # detect collision with wall.
    if x_cor > 280 or x_cor < -280 or y_cor > 280 or y_cor < -280:
        game_is_on = False
        scoreboard.game_over()


    # Detect collision of head and tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

    def restart():
        global game_is_on
        game_is_on = True
        food.refresh()
        scoreboard.reset_score()
        snake.reset_snake()


    screen.onkey(restart, "r")




screen.exitonclick()
