"""
scoreboard.py: A module containing the Scoreboard class for the Snake game.

The Scoreboard class represents the scoreboard in the Snake game. It tracks the player's score, displays the current
score and the high score on the screen, and provides methods for increasing the score, resetting the score, and drawing
the border on the screen.

"""

from turtle import Turtle
from os.path import exists

ALIGNMENT = "center"
FONT = ("TimesNewRoman", 14, "normal")


class Scoreboard(Turtle):
    """
    A class representing the scoreboard in the Snake game.

    Attributes:
        - score (int): The current score.
        - highscore (int): The high score obtained from the "highscore.txt" file.

    Methods:
        - __init__(): Initializes a new instance of the Scoreboard class.
        - increase_score(): Increases the score by one and updates the scoreboard display.
        - refresh_score(): Refreshes the scoreboard display with the current score and high score.
        - draw_border(x, y): Draws the border on the screen with the given coordinates.
        - reset_score(): Resets the score to zero and updates the scoreboard display. If the current score is higher than
          the previous high score, it updates the high score in the "highscore.txt" file.

    """

    def __init__(self):
        """
        Initializes a new instance of the Scoreboard class.

        The scoreboard starts with a score of zero. If the "highscore.txt" file exists, it reads the high score from the
        file and assigns it to the highscore attribute. Otherwise, the high score is set to zero.
        The turtle object for the scoreboard is configured to be hidden, penup, and positioned at the top center of the
        screen.

        """
        super().__init__()
        self.score = 0
        if exists("highscore.txt"):
            with open("highscore.txt") as file:
                self.highscore = int(file.read())
        else:
            self.highscore = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.setpos(0, 280)
        self.refresh_score()

    def increase_score(self):
        """
        Increases the score by one and updates the scoreboard display.

        """
        self.score += 1
        self.refresh_score()

    def refresh_score(self):
        """
        Refreshes the scoreboard display with the current score and high score.

        The current score and high score are displayed in the center of the top of the screen using the write method of
        the Turtle class.

        """
        self.clear()
        self.write(
            arg=f"Score: {self.score} High Score: {self.highscore}",
            move=False,
            align=ALIGNMENT,
            font=FONT,
        )

    def draw_border(self, x, y):
        """
        Draws the border on the screen with the given coordinates.

        This method creates a temporary turtle object and configures it to draw a border using the pencolor and penup
        methods of the Turtle class.

        Args:
            - x (int): The x-coordinate of the border.
            - y (int): The y-coordinate of the border.

        """
        temp = Turtle()
        temp.pencolor("white")
        temp.penup()
        temp.goto(x, -y)
        temp.pendown()
        temp.goto(-x, -y)
        temp.goto(-x, y)
        temp.goto(x, y)
        temp.goto(x, -y)

    def reset_score(self):
        """
        Resets the score to zero and updates the scoreboard display.

        If the current score is higher than the previous high score, it updates the high score in the "highscore.txt"
        file by writing the new high score. Then, it resets the score to zero and updates the scoreboard display.

        """
        if self.score > self.highscore:
            with open("highscore.txt", mode="w") as file:
                file.write(str(self.score))
            self.highscore = self.score
        self.score = 0
        self.refresh_score()
