import turtle

import pandas
import pandas as pd

screen = turtle.Screen()
t = turtle.Turtle()
t.penup()
t.hideturtle()

screen.title("U.S. States Game")
image = "blank_states_img.gif"

screen.addshape(image)

turtle.shape(image)

df = pd.read_csv("50_states.csv")
states = df["state"].tolist()

guessed_states = []
while len(guessed_states) < 50:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                            prompt="What's another state's name?")
    if answer_state == "exit":
        to_learn = []
        for state in states:
            if state not in guessed_states:
                to_learn.append(state)
        d = pd.DataFrame(to_learn, columns=["state"])
        d.to_csv("states_to_learn.csv")
        break
    for state in states:
        if answer_state.lower() == state.lower():
            guessed_states.append(state)
            found_state = df[df["state"] == f"{state}"]
            t.goto(int(found_state.x), int(found_state.y))
            t.write(f"{state}")



screen.exitonclick()
