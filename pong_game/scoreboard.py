from turtle import Turtle


class Scoreboard(Turtle):
    """
    A class representing the scoreboard in a game of Pong.
    Inherits from the Turtle class in the turtle module.
    """

    def __init__(self):
        """
        Initializes a new instance of the Scoreboard class.
        Sets the color, font, and initial scores of the players.
        """
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.update_scores()

    def update_scores(self):
        """
        Clears the scoreboard and updates the scores for each player.
        """
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Times New Roman", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Times New Roman", 80, "normal"))

    def r_point(self):
        """
        Increases the score of the right player by 1 and updates the scoreboard.
        """
        self.r_score += 1
        self.update_scores()

    def l_point(self):
        """
        Increases the score of the left player by 1 and updates the scoreboard.
        """
        self.l_score += 1
        self.update_scores()
