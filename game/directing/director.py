from game.casting.actor import Actor
from game.casting.cast import Cast
from game.casting.falling_object import FallingObject
from game.casting.player import Player
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

class Director(VideoService,KeyboardService):
    """
    Creates the Director class that is used to control the game.  Inherits VideoService and KeyboardService.
    """
    def __init__(self):
        """
        Initializes the object and sets the attributes
        """
        self.is_playing = True
