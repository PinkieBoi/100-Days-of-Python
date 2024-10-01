from tkinter import *
import tkinter.messagebox
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_data = quiz_brain
        self.win = Tk()
        self.win.title("Quizler")
        self.win.config(padx=20, pady=20, bg=THEME_COLOR)

        self.scoreboard = Label(
            text=f"Score: {self.quiz_data.score}",
            font=("Ubuntu", 12, "normal"),
            bg=THEME_COLOR,
            fg="#FFF"
        )
        self.scoreboard.grid(row=0, column=0, columnspan=2)

        self.canvas = Canvas(width=300, height=250)
        self.canvas.create_text(
            150,
            125,
            width=280,
            tags="question",
            text="Question",
            font=("Ubuntu", 15, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=10)

        self.check_mk = PhotoImage(file="images/true.png")
        self.cross_mk = PhotoImage(file="images/false.png")
        self.true_btn = Button(image=self.check_mk, command=self.is_true, highlightthickness=0, bg=THEME_COLOR)
        self.false_btn = Button(image=self.cross_mk, command=self.is_false, highlightthickness=0, bg=THEME_COLOR)
        self.true_btn.grid(row=2, column=0, padx=10, pady=10)
        self.false_btn.grid(row=2, column=1, padx=10, pady=10)
        self.display_question()
        self.win.mainloop()

    def display_question(self):
        q_text = self.quiz_data.next_question()
        self.canvas.itemconfigure(tagOrId="question", text=q_text)

    def update_score(self):
        self.scoreboard.config(text=f"Score: {self.quiz_data.score}")

    def no_more_questions(self):
        self.canvas.itemconfigure(tagOrId="question", text="End of Quiz")
        self.true_btn.config(state="disabled")
        self.false_btn.config(state="disabled")
        tkinter.messagebox.showinfo(
            title="Final Score",
            message=f"Score: {self.quiz_data.score}/{self.quiz_data.asked}"
        )

    def is_true(self):
        self.give_feedback("True")
        self.update_score()

    def is_false(self):
        self.give_feedback("False")
        self.update_score()

    def more_questions(self):
        self.canvas.config(bg="#FFF")
        if self.quiz_data.still_has_questions():
            self.display_question()
        else:
            self.no_more_questions()

    def give_feedback(self, response):
        if self.quiz_data.check_answer(self.quiz_data.current_question, response):
            self.canvas.config(bg="#63BC46")
        else:
            self.canvas.config(bg="#FF0000")
        self.win.after(600, self.more_questions)
