from turtle import Turtle,Screen
ALIGNMENT = "center"
FONT = ("Courier",16,"normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 270)
        self.color("white")
        self.write(f' Score: {self.score}', align = ALIGNMENT, font = FONT)
        self.hideturtle()

    def inc_score(self):
        self.score += 1
        self.clear()
        self.write(f' Score: {self.score}', align = ALIGNMENT, font = FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f'GAME OVER', align = ALIGNMENT, font = FONT)



