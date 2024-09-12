from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "JetBrainsMono"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = "✔"
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    win.after_cancel(timer)
    heading.config(text="Timer", fg=GREEN)
    canvas.itemconfig("timer_text", text="00:00")
    check_label.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        heading.config(text="Break", fg=RED)
        countdown(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        heading.config(text="Short Break", fg=PINK)
        countdown(SHORT_BREAK_MIN * 60)
    else:
        heading.config(text="Work", fg=GREEN)
        countdown(WORK_MIN * 60)
        win.after(WORK_MIN * 60 * 1000, add_checkmark)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(seconds):
    global timer
    if seconds >= 0:
        mins = seconds // 60
        secs = seconds % 60
        if secs < 10:
            secs = f"0{secs}"
        canvas.itemconfig("timer_text", text=f"{mins}:{secs}")
        timer = win.after(1000, countdown, seconds - 1)
    else:
        start_timer()


def add_checkmark():
    check_label["text"] += CHECK_MARK


# ---------------------------- UI SETUP ------------------------------- #
win = Tk()
win.title("Pomodoro Timer")
win.config(padx=100, pady=50, bg=YELLOW)

tom = PhotoImage(file="tomato.png")
canvas = Canvas(width=204, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(102, 112, image=tom)
canvas.create_text(103, 130, fill="white", font=(FONT_NAME, 35, "bold"), text="00:00", tags="timer_text")
canvas.grid(row=2, column=2)

# Heading / Current timer
heading = Label(text="Timer", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)
heading.grid(row=1, column=2, pady=20)

# Start Button
s_btn = Button(text="Start", font=(FONT_NAME, 10, "normal"), highlightthickness=0, command=start_timer)
s_btn.grid(row=3, column=1)

# Reset Button
r_btn = Button(text="Reset", font=(FONT_NAME, 10, "normal"), highlightthickness=0, command=reset_timer)
r_btn.grid(row=3, column=3)

# Completed Timers
check_label = Label(text="", bg=YELLOW, fg=GREEN)
check_label.grid(row=4, column=2)


win.mainloop()
