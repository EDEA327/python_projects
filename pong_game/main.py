from turtle import Screen
from paddle import Paddle

# Setting up the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.bgcolor("black")

# Creating the paddle
paddle = Paddle()

# Event listeners
screen.listen()
screen.onkeypress(paddle.up, "Up")
screen.onkeypress(paddle.down, "Down")
# Keep the window open
screen.mainloop()
