import json
import string
import random
import pyperclip
from tkinter import *
import tkinter.messagebox

FONT = ("Ubuntu", 10, "normal")
letters = list(string.ascii_lowercase)
nums = list(string.digits)
sym_chars = list(string.punctuation)


# Password Generator
def gen_passwd():
    rand_pass = [random.choice(letters).upper() for _ in range(4)]
    rand_pass += [random.choice(nums) for _ in range(4)]
    rand_pass += [random.choice(sym_chars) for _ in range(4)]
    rand_pass += [random.choice(letters) for _ in range(10)]
    random.shuffle(rand_pass)
    pass_info.insert(0, "".join(rand_pass))


# Save Password
def save_passwd():
    web_addr = site_info.get()
    user_n = user_info.get()
    pass_code = pass_info.get()
    new_data = {
        web_addr: {
            "Username": user_n,
            "Password": pass_code
        }
    }
    if len(web_addr) > 0 and len(user_n) > 0 and len(pass_code) > 0:
        try:
            with open("data.json", "r") as f:
                data = json.load(f)
                data.update(new_data)
        except FileNotFoundError:
            data = new_data
        finally:
            with open("data.json", "w") as f:
                json.dump(data, f, indent=4)
            site_info.delete(0, END)
            user_info.delete(0, END)
            pass_info.delete(0, END)
            site_info.focus()
            if tkinter.messagebox.askyesno(title=web_addr, message="Saved.\nCopy password to clipboard?"):
                pyperclip.copy(pass_code)
    else:
        tkinter.messagebox.showerror(title="Error", message="All fields required.")


# Site Search
def site_search():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            site_data = data[site_info.get()]
            if tkinter.messagebox.askyesno(
                title=f"{site_info.get()}",
                message=f"Username: {site_data['Username']}\n\nCopy password to clipboard?"
            ):
                pyperclip.copy(site_data["Password"])
    except KeyError:
        tkinter.messagebox.showerror(
            title="Error",
            message=f"No credentials stored for {site_info.get()}"
        )
    except FileNotFoundError:
        tkinter.messagebox.showerror(
            title="Error",
            message="Credential database is empty"
        )
    finally:
        site_info.delete(0, END)


# UI Setup
win = Tk()
win.title("MyPyPass")
win.config(padx=30, pady=30, width=400)

logo = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=0, columnspan=3)

# Field Labels
site_addr = Label(text="Website", font=FONT, width=10)
u_name = Label(text="Username", font=FONT)
p_word = Label(text="Password", font=FONT)
site_addr.grid(row=1, column=0)
u_name.grid(row=2, column=0)
p_word.grid(row=3, column=0)

# Input Boxes
site_info = Entry(width=22, highlightthickness=0)
user_info = Entry(width=35, highlightthickness=0)
pass_info = Entry(width=22, highlightthickness=0)
site_info.grid(row=1, column=1, pady=3)
user_info.grid(row=2, column=1, columnspan=2, pady=3)
pass_info.grid(row=3, column=1, pady=3)
site_info.focus()

# Buttons
search_btn = Button(text="Search", font=FONT, width=9, justify="right", command=site_search)
gen_pass = Button(text="Generate", font=FONT, width=9, justify="right", command=gen_passwd)
add_btn = Button(text="Add", font=FONT, width=32, command=save_passwd)
search_btn.grid(row=1, column=2)
gen_pass.grid(row=3, column=2)
add_btn.grid(row=4, column=1, columnspan=2, pady=5)

win.mainloop()
