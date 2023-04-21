from turtle import Screen
from paddle import Paddle

# Setting up the screen
screen: Screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.bgcolor("black")

# Creating the paddle
paddle: Paddle = Paddle()

# Event listeners
screen.listen()

# I used lambda to be able to define a function without arguments, which is what the onkeypress() method needs
screen.onkeypress(lambda: paddle.move("up"), "Up")
screen.onkeypress(lambda: paddle.move("down"), "Down")

# Keep the window open
screen.mainloop()

