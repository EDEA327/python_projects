from random import choice
from tkinter import *
from typing import Dict, Any, List

import pandas as pd

# Constants
BACKGROUND_COLOR: str = "#B1DDC6"
current_card: Dict[str, Any] = {}


# Code
def new_card() -> None:
    """
    Function to display a new flashcard.
    """
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(lang_data_list)
    canvas.itemconfig(word, text=current_card["English"], fill="black")
    canvas.itemconfig(language, text="English", fill="black")
    canvas.itemconfig(card_bg, image=canvas_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card() -> None:
    """
    Function to flip the flashcard and display the translation.
    """
    canvas.itemconfig(language, text="Español", fill="white")
    canvas.itemconfig(word, text=current_card["Español"], fill="white")
    canvas.itemconfig(card_bg, image=canvas_back_img)


def is_known() -> None:
    """
    Function to mark the flashcard as known and remove it from the list.
    """
    lang_data_list.remove(current_card)
    data = pd.DataFrame(lang_data_list)
    data.to_csv("data/words_to_learn.csv", index=False)
    new_card()


# Extract data from .csv file
try:
    lang_data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    lang_data = pd.read_csv("data/1000 words in english - Hoja 1.csv")
    lang_data_list: List[Dict[str, Any]] = lang_data.to_dict(orient="records")
else:
    lang_data_list = lang_data.to_dict(orient="records")

# Window Setup
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(window, width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_front_img = PhotoImage(file="images/card_front.png")
canvas_back_img = PhotoImage(file="images/card_back.png")
card_bg = canvas.create_image(400, 263, image=canvas_front_img)
canvas.grid(column=0, row=0, columnspan=2)

language = canvas.create_text(400, 150, text="Language", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))

wrong_img = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=wrong_img, highlightthickness=0, command=new_card)
wrong_btn.grid(column=0, row=1)

right_img = PhotoImage(file="images/right.png")
right_btn = Button(image=right_img, highlightthickness=0, command=is_known)
right_btn.grid(column=1, row=1)

new_card()

window.mainloop()
