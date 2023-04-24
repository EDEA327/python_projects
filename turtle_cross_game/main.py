import time
from turtle import Screen

from player import Player


def main():
    # Set up the screen
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("white")
    screen.title("Turtle Crossing Street")
    screen.tracer(0)

    # Creates a player
    player = Player()

    # Event listeners
    screen.listen()
    screen.onkeypress(player.move, "Up")

    # Game loop
    game_on = True
    while game_on:
        time.sleep(0.1)
        screen.update()

    # Keep the screen open
    screen.mainloop()


if __name__ == "__main__":
    main()
