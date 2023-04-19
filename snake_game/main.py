from turtle import Screen, Turtle

# Create a new screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

# Crete the  initial snake
# # Drawing white squares
# SQUARE_SIZE = 20
SQUARE_COLOR = "white"
SQUARE_SPACING = -20

turtles = []

# Create and add the three Turtle objects to the 'turtles' list
for i in range(3):
    t = Turtle(shape="square")
    t.color(SQUARE_COLOR)
    # t.shapesize(stretch_wid=SQUARE_SIZE, stretch_len=SQUARE_SIZE)
    t.penup()
    t.goto(x=i*SQUARE_SPACING, y=0)
    turtles.append(t)

# Keep the window open
screen.exitonclick()



