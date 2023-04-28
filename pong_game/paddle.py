from turtle import Turtle

from typing import Tuple


class Paddle(Turtle):
    """
    A class that represents a paddle object in a game of Pong.

    Attributes:
        None

    Methods:
        __init__(): Initializes the Paddle object.
        create(): Creates the Paddle object.
        move(direction: str): Moves the Paddle object up or down.
    """

    def __init__(self, pos: Tuple[int, int]) -> None:
        """
        Initializes the Paddle object.
        """
        super().__init__()
        self.pos = pos
        self.create(pos)

    def create(self, position: Tuple[int, int]) -> None:
        """
        Creates the Paddle object.
        """
        self.penup()
        self.goto(position)
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")

    def move(self, direction: str) -> None:
        """
        Moves the Paddle object up or down.

        Parameters:
        direction (str): The direction in which to move the Paddle object. Can be either 'up' or 'down'.

        Returns:
        None
        """
        max_y: int = 250
        min_y: int = -250
        current_y: float = self.ycor()

        if direction == 'up' and current_y < max_y:
            self.sety(current_y + 20)
        elif direction == 'down' and current_y > min_y:
            self.sety(current_y - 20)
