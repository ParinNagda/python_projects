import turtle
import  pandas

data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()
screen = turtle.Screen()

screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

guessed_list = []

while len(guessed_list) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_list)}/50 States Correct", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_list:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("learn_states.csv")
        break

    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        guessed_list.append(answer_state)
        t.write(state_data.state.item())
