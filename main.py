from turtle import  Turtle, Screen
import random
colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
is_race_on = False
all_turtles = []
def on_the_mark():
    i = 0
    for val in range(-3, 4):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(colors[i])
        i += 1
        new_turtle.penup()
        new_turtle.goto(-230, val * 50)
        all_turtles.append(new_turtle)

screen = Screen()

screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter color")

on_the_mark()

if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("You won")
            else:
                print(f"You lost the bet. {winning_color} won"
                      )
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

screen.exitonclick()
