from turtle import Turtle, Screen
from random import sample, randrange
from cars import *

BLUE_CAR = "cars/blue_car.gif"
PINK_CAR = "cars/pink_car.gif"
RED_CAR = "cars/red_car.gif"
YELLOW_CAR = "cars/yellow_car.gif"
CAR_COLORS = [BLUE_CAR, YELLOW_CAR, RED_CAR, PINK_CAR]


class CarManager:

    def __init__(self):
        for car in CAR_COLORS:
            Screen().addshape(car)
        self.cars = []
        self.move_increment = 4
        for c in range(25):
            self.generate_car()

    def generate_car(self):
        car = Turtle()
        car.shape(sample(CAR_COLORS, k=1)[0])
        car.penup()
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
