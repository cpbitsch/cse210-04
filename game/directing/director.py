from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

class Director(VideoService,KeyboardService):
    """
    Creates the Director class that is used to control the game.  Inherits VideoService and KeyboardService.
    """
    def __init__(self, keyboard_service, video_service):

        """
        Initializes the object and sets the attributes
        """

        self.keyboard_service = keyboard_service
        self.video_service = video_service

    def _start_game(self, cast):

        """Starts the game.
            Definitions:
                None."""

        self._video_service.open_window()
        while self._video_service.is_open_window():
            self._do_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _do_inputs(self, cast):

        """Gets movement inputs from player and applies it to the character.
            Definitions:
                player: The player character that is moving around.
                movement: The current direction of movement of the player."""

        player = cast.get_first_actor("player")
        movement = self._keyboard_service.get_direction()
        player.set_velocity(movement)

    def _do_updates(self, cast):

        """Updates game with inputs obtained, monitors for interactions.
            Definitions:
                banner: Words that display information about interactions.
                player: The player character that is moving around.
                falling_objects: Falling objects in the game.  Includes rocks and gems."""

        banner = cast.get_first_actor("banners")
        player = cast.get_first_actor("players")
        falling_objects = cast.get_actors("falling_objects")

        banner.set_text("")
        maximum_x = self._video_service.get_width()
        maximum_y = self._video_service.get_height()
        player.move_next(maximum_x,maximum_y)

        for falling_object in falling_objects:
            if player.get_position() == falling_object.get_position():
                message = falling_object.get_message()
                banner.set_text(message)

    def _do_outputs(self, cast):

        """Outputs information to the player, specifically creates the objects and character on the screen.
            Definitions:
            actors: All actors present in the game.  See actor.py for more details."""

        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()
