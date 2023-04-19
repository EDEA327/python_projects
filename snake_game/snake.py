from turtle import Turtle


class Snake:
    def __init__(self):
        self.snake_color = "white"
        self.square_spacing = -20
        self.distance = 20
        self.segments = []

        # Create a snake body with three segments
        for i in range(3):
            new_segment = Turtle(shape="square")
            new_segment.color(self.snake_color)
            new_segment.penup()
            new_segment.goto(x=i * self.square_spacing, y=0)
            self.segments.append(new_segment)

    def move(self):
        # Move the snake forward by one square
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.segments[0].forward(self.distance)

    def up(self):
        self.segments[0].setheading(90)

    def down(self):
        self.segments[0].setheading(270)

    def left(self):
        self.segments[0].setheading(180)

    def right(self):
        self.segments[0].setheading(0)

