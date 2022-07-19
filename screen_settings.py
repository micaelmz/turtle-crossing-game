from turtle import Screen, Turtle


class ScreenSettings:

    def __init__(self):
        Screen().setup(width=600, height=600)
        Screen().tracer(0)
        Screen().listen()
        self.screen_props = Turtle(visible=False)
        self.finish_line()
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

    def finish_line(self):
        self.screen_props.pensize(2)
        self.screen_props.pencolor('red')
        self.screen_props.penup()
        self.screen_props.goto(x=-300, y=260)
        for c in range(15):
            self.screen_props.pendown()
            self.screen_props.forward(20)
            self.screen_props.penup()
            self.screen_props.forward(20)
