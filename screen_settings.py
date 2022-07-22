from turtle import Screen, Turtle

BACKGROUND_IMAGE = 'road.gif'


class ScreenSettings:

    def __init__(self):
        Screen().setup(width=600, height=600)
        Screen().tracer(0)
        Screen().listen()
        Screen().title('Turtle Crossing Game')
        Screen().addshape(BACKGROUND_IMAGE)
        self.screen_props = Turtle(visible=False)
        self.screen_background = Turtle()
        self.screen_background.shape(BACKGROUND_IMAGE)
        self.wall_box()

    def wall_box(self):
        self.screen_props.pencolor('black')
        self.screen_props.penup()
        self.screen_props.goto(-300, 300)
        self.screen_props.pendown()
        self.screen_props.goto(300, 300)
        self.screen_props.goto(300, -300)
        self.screen_props.goto(-300, -300)
        self.screen_props.goto(-300, 300)
