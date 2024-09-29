import requests
from tkinter import *

FONT = ("Ubuntu", 20, "bold")


def next_quote():
    response = requests.get(url="https://api.kanye.rest/")
    response.raise_for_status()
    canvas.itemconfigure(tagOrId="quote", text=response.json()["quote"])


win = Tk()
win.title("Kanye Says...")
win.config(bg="#FFF")

quote_img = PhotoImage(file="background.png")
kanye_img = PhotoImage(file="kanye.png")

canvas = Canvas(width=500, height=460, bg="#FFF", highlightthickness=0)
canvas.create_image(250, 250, image=quote_img, tags="quote_bg")
canvas.create_text(250, 225, width=250, text="", tags="quote", font=FONT)
canvas.pack()

refresh_btn = Button(text="Refresh", command=next_quote, bg="#FFF", image=kanye_img)
refresh_btn.pack(pady=20)

next_quote()

win.mainloop()
