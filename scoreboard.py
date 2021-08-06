from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 240)
        self.hideturtle()
        self.player_one_score = 0
        self.player_two_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"{self.player_one_score}    {self.player_two_score}", align="center", font=("Arial", 50, "normal"))

    def player_one_get_point(self):
        self.player_one_score += 1

    def player_two_get_point(self):
        self.player_two_score += 1

    def end_game(self):
        self.color("red")
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Arial", 50, "normal"))