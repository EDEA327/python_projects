from tkinter import *


def button_clicked():
    label.config(text=inp.get())


window = Tk()
window.title("Tkinter playground")
window.minsize(width=500, height=500)

# label
label = Label(text="I'm a label", font=("Victor Mono", 24, "bold"))
label.grid(column=0, row=0)

# Button

button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New button")
new_button.grid(column=2, row=0)

# entry
inp = Entry(width=10)
inp.grid(column=3, row=2)
inp.get()


mainloop()
