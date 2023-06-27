from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzler App")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        # Labels
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=("Arial", 14, "italic"))
        self.score_label.grid(row=0, column=1)
        # Canvas stuff
        self.canvas = Canvas(height=250, width=300, bg="white")
        self.question = self.canvas.create_text(
                                                150,
                                                125,
                                                width=280,
                                                text="Place for the question",
                                                font=("Arial", 20, "italic"),
                                                fill=THEME_COLOR
                                                )

        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        # Button stuff
        img_true = PhotoImage(file="images/true.png")
        self.true_btn = Button(image=img_true, highlightthickness=0)
        self.true_btn.grid(column=0, row=2)

        img_false = PhotoImage(file="images/false.png")
        self.false_btn = Button(image=img_false, highlightthickness=0)
        self.false_btn.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question, text=q_text)


