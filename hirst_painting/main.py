# import colorgram
# Extracting the colors of the image..
# colors = colorgram.extract('image.jpg', 30)
# rgb_colors = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]
import turtle as t
import random

# The colors of the image.
colors_list = [(215, 153, 102), (15, 19, 74), (235, 225, 101), (49, 85, 146), (111, 172, 213), (170, 80, 46)]

# able to use rgb colors
t.colormode(255)

# Create a Turtle object
leo = t.Turtle()
leo.speed("fastest")
# Moving the turtle to the bottom left corner
# 225 is the middle angle between 180 an 270.
leo.setheading(225)
leo.hideturtle()
leo.penup()
leo.forward(300)
leo.setheading(0)
dot_count = 100
# Draw dots
for dot in range(1, dot_count + 1):
    color = random.choice(colors_list)
    leo.dot(20, color)
    leo.penup()
    leo.forward(50)

    if dot % 10 == 0:
        leo.setheading(90)
        leo.forward(50)
        leo.setheading(180)
        leo.forward(500)
        leo.setheading(0)


# Create a Screen object
screen = t.Screen()
screen.mainloop()
