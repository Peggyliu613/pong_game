from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10 * random.choice([1, -1])
        self.y_move = 10 * random.choice([1, -1])

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce(self):
        self.y_move *= -1

    def hit(self):
        self.x_move *= -1

    def end_round(self):
        self.goto(0, 0)
        self.x_move *= -1
