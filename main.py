import time
from turtle import Screen
from car_manager import CarManager
from scoreboard import Scoreboard
from player import Player
from screen_settings import ScreenSettings
import sound_effect


screen = ScreenSettings()
player = Player()
cars = CarManager()
score = Scoreboard()

Screen().onkeypress(player.move, key='w')
Screen().onkeypress(sound_effect.background_sound(stop=True), key='p')

sound_effect.background_sound()
game_running = True
while game_running:
    time.sleep(0.05)
    cars.move()
    score.update()
    Screen().update()

    for car in cars.cars:
        if car.distance(player) < 20:
            sound_effect.game_over()
            game_running = False
            player.game_over()
        if car.xcor() > 300:
            car.hideturtle()
        else:
            car.showturtle()

    if player.ycor() == 260:
        cars.level_up()
        player.level_up()
        score.level += 1

Screen().exitonclick()
