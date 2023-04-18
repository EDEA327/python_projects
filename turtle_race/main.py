import turtle
from turtle import Turtle, Screen
import random
import tkinter.messagebox
message = """Which turtle will win the race?
red
orange
yellow
green
blue
purple 
enter a color: """
is_race_on = False
screen = Screen()
screen.setup(width=500, height=500)
user_bet = screen.textinput(title="Make your bet", prompt=message)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
turtles = []

# Creating the turtles
for index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[index])
    new_turtle.goto(x=-230, y=y_positions[index])
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            win_color = turtle.pencolor()
            if win_color == user_bet:
                tkinter.messagebox.showinfo("Race result", f"You've won the {win_color} turtle color is the winner!")
            else:
                tkinter.messagebox.showinfo("Race result", f"You've lose the {win_color} turtle color is the winner!")

        dist = random.randint(0, 10)
        turtle.forward(dist)

screen.exitonclick()
