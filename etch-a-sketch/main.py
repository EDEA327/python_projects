# Imports
import turtle as t

leo = t.Turtle()
screen = t.Screen()


def move_forwards():
    leo.forward(10)


def move_backwards():
    leo.backward(10)


def counter_clockwise():
    leo.left(15)


def clockwise():
    leo.right(15)


def clear():
    leo.clear()
    leo.penup()
    leo.home()
    leo.pendown()


# Start to listen
screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(counter_clockwise, "a")
screen.onkey(clockwise, "d")
screen.onkey(clear, "c")
screen.exitonclick()


