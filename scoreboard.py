from turtle import Turtle
ALIGNMENT = "center"
FONT = ("TimesNewRoman", 14, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.setpos(0, 280)
        self.refresh_score()

    # Clears current turtle, increases the score by one and refreshes the turtle
    def increase_score(self):
        self.score += 1
        self.refresh_score()

    def refresh_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.highscore}", move=False, align=ALIGNMENT, font=FONT)

    def draw_border(self, x, y):
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
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.refresh_score()
