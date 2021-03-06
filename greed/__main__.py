import os
import random

from game.casting.actor import Actor
from game.casting.cast import Cast
from game.casting.gem import Gem
from game.casting.rock import Rock

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point


FRAME_RATE = 10
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Greed"
WHITE = Color(255, 255, 255)
DEFAULT_ARTIFACTS = 40


def main():
    
    # create the cast
    cast = Cast()
    point = Point(0, 0)
    
    # create the banner
    banner = Actor()
    banner.set_text("")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(CELL_SIZE, 0)
    cast.add_actor("banners", banner)
    
    # create the person
    x = int(COLS / 2)
    y = ROWS - 2
    position = Point(x, y)
    position = position.scale(CELL_SIZE)
    

    player = Actor()
    player.set_text("<|^|>")
    player.set_font_size(FONT_SIZE)
    player.set_color(WHITE)
    player.set_position(x, y)
    cast.add_actor("player", player)
    
    for n in range(int((DEFAULT_ARTIFACTS / 2))):
        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 10)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        gem = Gem()
        gem.set_text("*")
        gem.set_font_size(FONT_SIZE)
        gem.set_color(color)
        gem.set_position(x, y)
        cast.add_actor("gem", gem)

    for n in range(int((DEFAULT_ARTIFACTS))):
        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 10)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        rock = Rock()
        rock.set_text("O")
        rock.set_font_size(FONT_SIZE)
        rock.set_color(color)
        rock.set_position(x, y)
        cast.add_actor("rock", rock)
    
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast, gem, rock, point)


if __name__ == "__main__":
    main()