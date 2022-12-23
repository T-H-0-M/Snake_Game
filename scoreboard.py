from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.setpos(0, 280)
        self.penup()
        self.color("white")
        self.refresh_score()

    def increase_score(self):
        self.clear()
        self.score = self.score + 1
        self.refresh_score()

    def refresh_score(self):
        self.write(arg="Score: " + str(self.score), move=False, align="center", font=("TimesNewRoman", 10, "normal"))