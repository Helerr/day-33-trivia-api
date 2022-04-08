from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(background=THEME_COLOR, padx=20, pady=20)

        self.canvas = Canvas()
        self.canvas.config(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125,
                                                     text="Amazon acquired Twitch in August 2014 for $970 million dollars.",
                                                     font=("Arial", 16, "italic"), width=280, fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        self.score_label = Label(text="Score: 0", font=("Arial", 12, "bold"), background=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        correct_image = PhotoImage(file="images/true.png")
        wrong_image = PhotoImage(file="images/false.png")

        self.true_button = Button(image=correct_image, highlightthickness=0, bd=0, command=self.true_pressed)
        self.false_button = Button(image=wrong_image, highlightthickness=0, bd=0, command=self.false_pressed)

        self.true_button.grid(row=2, column=0, padx=20, pady=20)
        self.false_button.grid(row=2, column=1, padx=20, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(background="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(500, self.get_next_question)