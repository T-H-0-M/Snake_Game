from turtle import Turtle
ALIGNMENT = "center"
FONT = ("TimesNewRoman", 14, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.setpos(0, 280)
        self.refresh_score()

    # Clears current turtle, increases the score by one and refreshes the turtle
    def increase_score(self):
        self.clear()
        self.score += 1
        self.refresh_score()

    def refresh_score(self):
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

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

    def gameover(self):
        self.setpos(0, 0)
        self.write(arg="GAME OVER", move=False, align=ALIGNMENT, font=FONT)
