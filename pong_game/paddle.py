from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(x=350, y=0)
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")

    def move(self, direction):
        max_y = 250
        min_y = -250
        current_y = self.ycor()
        if direction == 'up' and current_y < max_y:
            self.sety(current_y + 20)
        elif direction == 'down' and current_y > min_y:
            self.sety(current_y - 20)




