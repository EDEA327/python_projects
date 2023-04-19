from turtle import Screen, Turtle
import time

# Create a new screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
# Turns off the animation.
screen.tracer(0)

# Create the  initial snake
# SQUARE_SIZE = 20
SQUARE_COLOR = "white"
SQUARE_SPACING = -20

segments = []

# Create and add the three Turtle objects to the 'turtles' list
# # Create a snake body
for i in range(3):
    new_segment = Turtle(shape="square")
    new_segment.color(SQUARE_COLOR)
    # t.shapesize(stretch_wid=SQUARE_SIZE, stretch_len=SQUARE_SIZE)
    new_segment.penup()
    new_segment.goto(x=i * SQUARE_SPACING, y=0)
    segments.append(new_segment)
# Update the screen
screen.update()
# Start the game
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for segment in segments:
        segment.forward(20)

# Keep the window open
screen.exitonclick()



