import turtle
import pandas as pd

win = turtle.Screen()
win.title("U.S. States Game")
img = "blank_states_img.gif"
win.addshape(img)
turtle.shape(img)

label = turtle.Turtle()
label.hideturtle()
label.penup()

data = pd.read_csv("50_states.csv")
states = data.state.tolist()
guessed_states = []

while len(guessed_states) < 50:
    guess = turtle.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="Enter a state name").title()
    if guess == "Exit":
        missed_states = [state for state in states if state not in guessed_states]
        df = pd.DataFrame({"Missed States": missed_states})
        df.to_csv("Missed_States.csv")
        break
    elif guess in states and guess not in guessed_states:
        state_data = data[data.state == guess]
        label.goto(float(state_data.x), float(state_data.y))
        label.write(guess)
        guessed_states.append(guess)
