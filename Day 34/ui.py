from tkinter import *
from quiz_brain import QuizBrain

THEME = "#375362"
FONT = ("Arial", 20, "italic")


class UserUI:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzy")
        self.window.config(padx=20, pady=20, bg=THEME)

        self.score_label = Label(fg="white", bg=THEME, text=f"Score:{self.quiz.score}")
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(
            width=300,
            height=250,
            bg="white",
        )
        self.qsn_txt = self.canvas.create_text(
            150, 125, text="", fill=THEME, font=FONT, width=280
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        right_img = PhotoImage(file="images/true.png")
        self.right_btn = Button(
            image=right_img, highlightthickness=0, command=self.true_pressed
        )
        self.right_btn.grid(row=2, column=1)

        wrong_img = PhotoImage(file="images/false.png")
        self.wrong_btn = Button(
            image=wrong_img, highlightthickness=0, command=self.false_pressed
        )
        self.wrong_btn.grid(row=2, column=0)

        self.next_qsn()
        self.window.mainloop()

    def next_qsn(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(
                text=f"Score:{self.quiz.score}/{self.quiz.question_number}"
            )
            q_txt = self.quiz.next_question()
            self.canvas.itemconfig(self.qsn_txt, text=q_txt)

        else:
            self.canvas.itemconfig(self.qsn_txt, text="You have reached the end:")
            self.score_label.config(
                text=f"Score:{self.quiz.score}/{self.quiz.question_number}"
            )
            self.right_btn.config(state="disabled")
            self.wrong_btn.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer(True)
        self.give_feedback(is_right)

    def false_pressed(self):
        is_wrong = self.quiz.check_answer(False)
        self.give_feedback(is_wrong)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, func=self.next_qsn)
