from turtle import Turtle

# Constants
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        """
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
        Creates a snake body with three segments.
        If self.growth is greater than zero,
        the length of the snake is increased by the value of self.growth
        """
        # Creates a snake with three segments
        for _ in range(3):
            self.add_segment()

    def add_segment(self):
        """
        Adds a new segment to the snake's body.
        """
        # Creates a new segment with a square shape, sets its color and position,
        # and appends it to the snake's segments list

        new_segment = Turtle(shape="square")
        new_segment.color(self.snake_color)
        new_segment.penup()
        if len(self.segments) == 0:
            new_segment.goto(0, 0)
        else:
            last_segment = self.segments[-1]
            new_segment.goto(last_segment.position())
        self.segments.append(new_segment)

    def extend(self):
        """
        Extends the length of the snake by adding a new segment.
        """
        self.add_segment()

    def move(self):
        """
        Moves the snake forward by one square.
        """
        # Moves each segment of the snake to the position of the segment in front of it, except for the head,
        # which is moved forward by one square.
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.head.forward(self.distance)

    def up(self):
        """
        Changes the direction of the snake's head to up, but only if the current direction is not down.
        """
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """
        Changes the direction of the snake's head to down, but only if the current direction is not up.
        """
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """
        Changes the direction of the snake's head to left, but only if the current direction is not right.
        """
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """
        Changes the direction of the snake's head to right, but only if the current direction is not left.
        """
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
