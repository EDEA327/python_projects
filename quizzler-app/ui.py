from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler App")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        # Labels
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        # Canvas stuff
        self.canvas = Canvas(height=250, width=300, bg="white")
        self.question = self.canvas.create_text(150, 125, text="Place for the question", font=("Arial", 14, "italic"), fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2)
        # Button stuff
        self.img_true = PhotoImage(file="images/true.png")
        self.img_false = PhotoImage(file="images/false.png")
        self.true_btn = Button(image=self.img_true)
        self.true_btn.grid(column=0, row=2)
        self.false_btn = Button(image=self.img_false)
        self.false_btn.grid(column=1, row=2)

        self.window.mainloop()

