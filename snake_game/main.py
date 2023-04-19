from turtle import Screen, Turtle

# Create a new screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

# Crete the  initial snake
# # Drawing white squares
turtles = []
for _ in range(3):
    t = Turtle(shape="square")
    t.color("white")
    turtles.append(t)

# # Placing the squares next to each other
turtles[1].goto(x=-20, y=0)
turtles[2].goto(x=-40, y=0)

# Keep the window open
screen.exitonclick()



