import turtle as t

img = "blank_states_img.gif"
screen = t.Screen()
screen.title("US Game")
screen.setup(width=800, height=600)
screen.addshape(img)

t.shape(img)

screen.mainloop()
