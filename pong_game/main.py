from turtle import Screen
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
        screen.update()

    # Keep the window open
    screen.mainloop()


if __name__ == "__main__":
    main()
