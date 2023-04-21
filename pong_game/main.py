from turtle import Screen
from paddle import Paddle

# Setting up the screen
screen: Screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.bgcolor("black")

# Creating the paddles
r_paddle: Paddle = Paddle((350, 0))
l_paddle: Paddle = Paddle((-350, 0))

# Event listeners
screen.listen()
# # I used lambda to be able to define a function without arguments, which is what the onkeypress() method needs
screen.onkeypress(lambda: r_paddle.move("up"), "Up")
screen.onkeypress(lambda: r_paddle.move("down"), "Down")
screen.onkeypress(lambda: l_paddle.move("up"), "w")
screen.onkeypress(lambda: l_paddle.move("down"), "s")

# Keep the window open
screen.mainloop()

