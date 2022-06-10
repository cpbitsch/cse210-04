from game.casting.actor import Actor
from game.shared.color import Color
from game.shared.point import Point
import random

class Gem(Actor):

    def __init__(self):
        super().__init__
        self.set_velocity(Point(0, 15))

    def create_new(self):
        x = random.randint(1, 59)
        y = 1
        position = Point(x, y)
        position = position.scale(15)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)

        self.set_text("*")
        self.set_font_size(15)
        self.set_color(color)
        self.set_position(position)
