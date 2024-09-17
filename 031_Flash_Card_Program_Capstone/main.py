import random
import pandas as pd
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
WHITE = "#FFF"
BLACK = "#000"
word = {}

try:
    data = pd.read_csv("data/words_to_learn.csv")
    lesson = data.to_dict(orient="records")
except FileNotFoundError:
    data = pd.read_csv("data/es_to_en.csv")
    lesson = data.to_dict(orient="records")

try:
    correct_words = pd.read_csv("data/es_learned.csv")
    correct_words.to_dict(orient="records")
except FileNotFoundError:
    correct_words = []


def new_card():
    global word, flip_timer
    win.after_cancel(flip_timer)
    word = random.choice(lesson)
    canvas.itemconfigure(tagOrId="card", image=f_card)
    canvas.itemconfigure(tagOrId="language", text="Spanish", fill=BLACK)
    canvas.itemconfigure(tagOrId="word", text=word["Spanish"], fill=BLACK)
    flip_timer = win.after(5000, show_translation)


def show_translation():
    global word
    canvas.itemconfigure(tagOrId="card", image=b_card)
    canvas.itemconfigure(tagOrId="language", text="English", fill=WHITE)
    canvas.itemconfigure(tagOrId="word", text=word["English"], fill=WHITE)


def correct_word():
    global word, correct_words, lesson
    correct_words.append(word)
    lesson.remove(word)
    l_df = pd.DataFrame(correct_words)
    to_learn = pd.DataFrame(lesson)
    l_df.to_csv("data/es_learned.csv", index=False)
    to_learn.to_csv("data/words_to_learn.csv", index=False)
    new_card()


# UI Setup
win = Tk()
win.title("Flashy")
win.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = win.after(5000, show_translation)

checkmark = PhotoImage(file="images/right.png")
crossmark = PhotoImage(file="images/wrong.png")
f_card = PhotoImage(file="images/card_front.png")
b_card = PhotoImage(file="images/card_back.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400, 263, image=f_card, tag="card")
canvas.create_text(400, 150, text="Spanish", font=("Ubuntu", 30, "italic"), tags="language", width=350)
canvas.create_text(400, 283, text="Word", font=("Ubuntu", 60, "italic"), tags="word")
canvas.grid(row=0, column=0, columnspan=2)

tick_btn = Button(image=checkmark, highlightthickness=0, command=correct_word)
cross_btn = Button(image=crossmark, highlightthickness=0, command=new_card)
tick_btn.grid(row=1, column=0)
cross_btn.grid(row=1, column=1)

if __name__ == "__main__":
    new_card()

win.mainloop()
