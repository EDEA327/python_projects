from turtle import Turtle
# Constants
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        """
        No Parameters

        Initializes a new Snake object with default values for snake color, spacing, distance, segments, and head.
        Creates a snake body with three segments.
        """
        self.snake_color = "white"
        self.square_spacing = -20
        self.distance = 20
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """
        No Parameters

        Creates a snake body with three segments.
        """
        for i in range(3):
            new_segment = Turtle(shape="square")
            new_segment.color(self.snake_color)
            new_segment.penup()
            new_segment.goto(x=i * self.square_spacing, y=0)
            self.segments.append(new_segment)

    def move(self):
        """
        No Parameters

        Moves the snake forward by one square.
        """
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.head.forward(self.distance)

    def up(self):
        """
        No Parameters

        Changes the direction of the snake's head to up, but only if the current direction is not down.
        """
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """
        No Parameters

        Changes the direction of the snake's head to down, but only if the current direction is not up.
        """
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """
        No Parameters

        Changes the direction of the snake's head to left, but only if the current direction is not right.
        """
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """
        No Parameters

        Changes the direction of the snake's head to right, but only if the current direction is not left.
        """
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


