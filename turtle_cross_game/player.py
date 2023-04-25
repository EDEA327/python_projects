from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.reset_position()

    def reached_goal(self):
        return self.ycor() > FINISH_LINE_Y

    def reset_position(self):
        self.goto(x=0, y=-280)

    def move(self):
        self.forward(MOVE_DISTANCE)
