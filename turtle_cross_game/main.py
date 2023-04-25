import time
from turtle import Screen

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard


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

    # Crete the level indicator
    level = Scoreboard()

    # Event listeners
    screen.listen()
    screen.onkeypress(player.move, "Up")

    # Game loop
    game_on = True
    frequency = 0
    while game_on:
        time.sleep(0.1)
        screen.update()
        # every 0.6 seconds a new car is created
        if frequency % 6 == 0:
            car_manager.create_car()

        car_manager.move_cars()

        frequency += 1

        # Detect collisions with cars
        for car in car_manager.all_cars:
            if car.distance(player) < 20:
                game_on = False
                level.game_over()

        # Successful cross
        if player.reached_goal():
            level.update_level()
            player.reset_position()
            car_manager.increment_speed()

    # Keep the screen open
    screen.mainloop()


if __name__ == "__main__":
    main()
