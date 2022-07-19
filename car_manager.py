from turtle import Turtle
from random import sample, randrange
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class CarManager:

    def __init__(self):
        super().__init__()
        self.cars = []
        self.move_increment = 4
        for c in range(25):
            self.generate_car()

    def generate_car(self):
        car = Turtle()
        car.color(sample(COLORS, k=1))
        car.penup()
        car.shape('square')
        car.shapesize(stretch_wid=0.8, stretch_len=1.75)
        car.setheading(180)
        car.goto(x=randrange(-300, 700, 20), y=randrange(-200, 250, 20))
        self.cars.append(car)

    def move(self):
        for car in self.cars:
            if car.xcor() < -300:
                car.goto(x=randrange(350, 1000, 20), y=randrange(-200, 250, 20))
            else:
                car.forward(self.move_increment)

    def level_up(self):
        self.move_increment += 1
