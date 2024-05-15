import time
import turtle
from turtle import Turtle, Screen
import random
tim = Turtle()
turtle.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r, g, b)
    return color

tim.shape("turtle")
tim.color("red")
tim.fillcolor("red")
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)

# for _ in range(0, 15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
colors = ["Violet","Indigo","Blue", "Green", "Yellow", "Orange", "Red", "Black"]
# i=0
# for val in range(3,11):
#     degree = 360
#     angle = 360 / val
#     tim.color(colors[i])
#     for _ in range(val):
#         tim.forward(100)
#         tim.left(angle)
#     i +=1

# directions = [0, 90, 180, 270]
# i = 0;
# tim.pensize(15)
# tim.speed("fastest")
# while i < 200:
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))
#     i+=1
for _ in range(0,100):
    tim.speed("fastest")
    tim.color(random_color())
    tim.circle(100)
    heading = tim.heading()
    tim.setheading(heading + 10)
    tim.circle(100)

screen = Screen()
screen.exitonclick()