import random
import turtle
from turtle import Turtle, Screen
from geometric_figures import Figure


# def draw_figure(fig, turtle, dist):
#     turtle.speed(3)
#     base_angle = 360
#     colores_turtle = ["black", "red", "green", "blue", "cyan", "yellow", "magenta", "orange", "gray", "pink",
#                       "brown", "tan", "purple", "gold", "silver", "navy"]
#     random_color = random.choice(colores_turtle)
#     turtle.color(random_color)
#     for i in range(fig.sides):
#         turtle.forward(dist)
#         turtle.right(base_angle / fig.sides)


# Create a turtle object
# It is necessary to be able to choose a random color
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return r, g, b


# Draw a spirograph
def draw_spirograph(size_of_gap):
    # 360 / size_of_gap It is used to make the necessary turns to create the circle.
    for _ in range(int(360 / size_of_gap)):
        kylian.color(random_color())
        kylian.circle(50)
        kylian.setheading(kylian.heading() + size_of_gap)


turtle.colormode(255)
kylian = Turtle()
kylian.speed("fastest")
kylian.hideturtle()


# Draw a random walk.
# directions = [0, 90, 180, 270]
# dist = 30
# kylian.pensize(8)
#
# for _ in range(100):
#     kylian.forward(dist)
#     kylian.setheading(random.choice(directions))
#     kylian.pencolor(random_color())


# Drawing different shapes
# figures = [Figure(i) for i in range(3, 11)]
# distance = 80
# for figure in figures:
#     draw_figure(figure, kylian, distance)

# Drawing a square.
# for _ in range(4):
#     kylian.fd(100)
#     kylian.rt(90)

# Drawing a dashed line
# Set the color and gross
# kylian.pensize(3)
# kylian.pencolor('blue')
# for i in range(10):
#     kylian.pendown()
#     kylian.forward(10)
#     kylian.penup()
#     kylian.forward(10)

# Create a screen object
screen = Screen()
screen.mainloop()

