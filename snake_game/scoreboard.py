from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.draw_score()

    def draw_score(self):
        self.penup()
        self.goto(x=-80, y=265)
        self.write(f"Score: {self.score}", font=("Times New Roman", 24, "normal"))
