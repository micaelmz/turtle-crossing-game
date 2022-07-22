from turtle import Turtle
from player import Player
FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.level = 0
        self.color('black')
        self.hideturtle()
        self.goto(-280, 260)
        self.write(f'Level: {self.level}', font=FONT)

    def update(self):
        self.clear()
        self.write(f'Level: {self.level}', font=FONT)