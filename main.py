import time
from turtle import Screen
from snake import Snake
from food import  Food
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
# screen.update()
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        snake.grow_snake()
        food.refresh()

    if snake.touched_wall():
        scoreboard.game_over()
        game_is_on = False

    if snake.snake_bitten():
        scoreboard.game_over()
        game_is_on = False

screen.exitonclick()

