import random
from turtle import Screen
import time
from ball import Ball
from paddle import Paddle


def main() -> None:
    """
    The main function that sets up the game and starts the game loop.
    """
    # Setting up the screen
    screen: Screen = Screen()
    screen.setup(width=800, height=600)
    screen.title("Pong Game")
    screen.bgcolor("black")
    screen.tracer(0)

    # Creating the paddles
    r_paddle: Paddle = Paddle((350, 0))
    l_paddle: Paddle = Paddle((-350, 0))

    # Creating the ball
    ball: Ball = Ball()

    # Event listeners
    screen.listen()
    # I used lambda to be able to define a function without arguments, which is what the onkeypress() method needs
    screen.onkeypress(lambda: r_paddle.move("up"), "Up")
    screen.onkeypress(lambda: r_paddle.move("down"), "Down")
    screen.onkeypress(lambda: l_paddle.move("up"), "w")
    screen.onkeypress(lambda: l_paddle.move("down"), "s")

    # Start the game loop
    game_on: bool = True

    while game_on:
        time.sleep(0.1)
        screen.update()
        ball.move()

        # Detect collision with walls
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()

        # Check if the ball has collided with a paddle
        if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (
                    ball.distance(l_paddle) < 50 and ball.xcor() < -320):
            ball.bounce_x()

        # Check if the ball has gone out of bounds
        if ball.xcor() > 380:
            ball.reset_position()
            ball.setheading(random.choice([135, 225]))  # Move to a random corner
        elif ball.xcor() < -380:
            ball.reset_position()
            ball.setheading(random.choice([45, 315]))  # Move to a random corner

    # Keep the window open
    screen.mainloop()


if __name__ == "__main__":
    main()
