import time
from turtle import Screen

from car_manager import CarManager
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

    # Create the cars
    car_manager = CarManager()

    # Event listeners
    screen.listen()
    screen.onkeypress(player.move, "Up")

    # Game loop
    game_on = True
    frequency = 0
    while game_on:
        time.sleep(0.1)
        screen.update()

        if frequency % 6 == 0:
            car_manager.create_car()

        car_manager.move_cars()
        
        frequency += 1


    # Keep the screen open
    screen.mainloop()


if __name__ == "__main__":
    main()
