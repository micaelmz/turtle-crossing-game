from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
FONT = ("Courier", 24, "bold")


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.color('dark olive green')
        self.shape('turtle')
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def game_over(self):
        self.hideturtle()
        self.goto(0, 0)
        self.color('black')
        self.write(f'GAME OVER', font=FONT, align='center')

    def level_up(self):
        self.goto(STARTING_POSITION)
