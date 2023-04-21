from turtle import Turtle


class Ball(Turtle):
    """
    A class representing a ball in a game of Pong.
    Inherits from the Turtle class in the turtle module.
    """

    def __init__(self):
        """
        Initializes a new instance of the Ball class.
        Sets the color, shape, and movement attributes of the ball.
        """
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.move_speed = 0.1
        self.x_move = 10
        self.y_move = 10

    def move(self):
        """
        Moves the ball by updating its position based on its current x and y
        movement values.
        """
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """
        Reverses the y movement of the ball, causing it to bounce off the top
        or bottom wall.
        """
        self.y_move *= -1

    def bounce_x(self):
        """
        Reverses the x movement of the ball, causing it to bounce off a paddle
        or the side wall.
        """
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        """
        Resets the position of the ball to the center of the screen and reverses
        its x movement, causing it to move in the opposite direction.
        """
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
