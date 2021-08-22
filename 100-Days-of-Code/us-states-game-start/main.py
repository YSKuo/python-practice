import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

data = pandas.read_csv("50_states.csv")

state_on_map = turtle.Turtle()
state_on_map.penup()
state_on_map.hideturtle()

all_states = data.state.to_list()
title = "Guess the state"
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=title, prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        state_data = data[data.state == answer_state]
        state_on_map.goto(int(state_data.x), int(state_data.y))
        state_on_map.write(answer_state)
        title = f"({len(guessed_states)}/50) Right Answer."
    else:
        title = f"({len(guessed_states)}/50) Wrong Answer."
