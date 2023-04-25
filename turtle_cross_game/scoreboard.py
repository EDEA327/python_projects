from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level: int = 0
        self.color("white")
        self.penup()
        self.goto(-265, 265)
        self.hideturtle()

    def update_level(self) -> None:
        """
        Updates the displayed level on the scoreboard turtle.
        """
        self.clear()
        self.write(f"level: {self.level}", font=FONT)
        self.level += 1

    def game_over(self) -> None:
        """
        Displays the game over message on the scoreboard turtle.
        """
        self.color("red")
        self.home()
        self.write("GAME OVER", font=FONT)
