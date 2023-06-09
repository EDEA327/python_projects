# Imports
from tkinter import *

# Constants
BACKGROUND_COLOR = "#B1DDC6"

# Code
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(window, width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=canvas_img)
canvas.grid(column=0, row=0, columnspan=2)

language = canvas.create_text(400, 150, text="Language", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))

wrong_img = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=wrong_img, highlightthickness=0)
wrong_btn.grid(column=0, row=1)

right_img = PhotoImage(file="images/right.png")
right_btn = Button(image=right_img, highlightthickness=0)
right_btn.grid(column=1, row=1)

window.mainloop()
