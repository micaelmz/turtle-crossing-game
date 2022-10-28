# Turtle

A turtle moves forwards when you press the "Up" key. It can only move forwards, not back, left or right.

## Cars

Cars are randomly generated along the y-axis and will move from the right edge of the screen to the left edge.


![Alt Text](https://media.giphy.com/media/UTOLFmvXw7Efpq93KA/giphy.gif)

## Next level & Game over

When the turtle hits the top edge of the screen, it moves back to the original position and the player levels up. On the next level, the car speed increases.

When the turtle collides with a car, it's game over and everything stops.

![Alt Text](https://media.giphy.com/media/tM4elLkYNrMrtXQuB6/giphy.gif)


## Initial Settings
### Screen setup
```python
from turtle import Screen

class ScreenSettings:

    def __init__(self):
        Screen().setup(width=600, height=600)
        Screen().tracer(0)
```
### Car manager

```python
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    pass
```

## Break down ideas
Sound effect, level, player, scoreboard

Improve graphs

### Run
```bash
python main.py
```

## Reference
[Day 23 - 100 Days of Code](https://www.udemy.com/course/100-days-of-code/learn/lecture/20343209#overview)