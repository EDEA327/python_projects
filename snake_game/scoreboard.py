from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Times New Roman", 24, "normal")


class ScoreBoard(Turtle):
    """
    A class to represent the scoreboard in the game.

    Attributes
    ----------
    score : int
        The current score of the player.

    Methods
    -------
    update_score():
        Updates the displayed score on the scoreboard turtle.
    """

    def __init__(self):
        """
        Constructs the scoreboard object and initializes its attributes.
        """
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        """
        Updates the displayed score on the scoreboard turtle.
        """
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        self.score += 1

    def game_over(self):
        self.home()
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

