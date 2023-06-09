# Imports
from random import choice
from tkinter import *

import pandas as pd

# Constants
BACKGROUND_COLOR = "#B1DDC6"


# Code
def new_card():
    current_card = choice(lang_data_list)
    canvas.itemconfig(word, text=current_card["English"])


# Window Setup
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(window, width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_front_img = PhotoImage(file="images/card_front.png")
canvas_back_img = PhotoImage(file="images/card_back.png")
canvas.create_image(400, 263, image=canvas_front_img)
canvas.grid(column=0, row=0, columnspan=2)

language = canvas.create_text(400, 150, text="English", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))

wrong_img = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=wrong_img, highlightthickness=0, command=new_card)
wrong_btn.grid(column=0, row=1)

right_img = PhotoImage(file="images/right.png")
right_btn = Button(image=right_img, highlightthickness=0, command=new_card)
right_btn.grid(column=1, row=1)

# # Extract data from .csv file
lang_data = pd.read_csv("data/1000 words in english - Hoja 1.csv")
lang_data_list = lang_data.to_dict(orient="records")
# print(lang_data_list)

window.mainloop()
