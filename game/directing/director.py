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

        "Starts the game."

        self._video_service.open_window()
        while self._video_service.is_open_window():
            self._do_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _do_inputs(self, cast):

        "Gets movement inputs from player."

        player = cast.get_direction()

    def _do_updates(self):

        "Updates game with inputs obtained."

    def _do_outputs(self):

        "Outputs information to the player."
