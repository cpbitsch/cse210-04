import random


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self.score = 0
        
    def start_game(self, cast, gem, rock, point):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast, gem, rock, point)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.
        
        Args:
            cast (Cast): The cast of actors.
        """
        player = cast.get_first_actor("player")
        velocity = self._keyboard_service.get_direction()
        player.set_velocity(velocity)

    def _do_updates(self, cast, gem, rock, point):
        """Updates the robot's position and resolves any collisions with artifacts.
        
        Args:
            cast (Cast): The cast of actors.
        """
 
        banner = cast.get_first_actor("banners")
        player = cast.get_first_actor("player")
        gems = cast.get_actors("gem")
        rocks = cast.get_actors("rock")

        banner.set_text("")
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        player.move_next(max_x, max_y)


        for gem in gems:
            gem.move_next(max_x, max_y)
            # Check if gem possition is equal to Player
            if (player.get_position().get_x() > gem.get_position().get_x() - 20 and player.get_position().get_x() < gem.get_position().get_x() + 10
            and player.get_position().get_y() > gem.get_position().get_y() - 20 and player.get_position().get_y() < gem.get_position().get_y() + 10):
                print("hit a Gem!!!")
                self.score += 1
                gem.move_next(max_x, 1)
        
        for rock in rocks:
            rock.move_next(max_x, max_y)
            # Check if rock possition is equal to Player
            if (player.get_position().get_x() > rock.get_position().get_x() - 20 and player.get_position().get_x() < rock.get_position().get_x() + 10
            and player.get_position().get_y() > rock.get_position().get_y() - 20 and player.get_position().get_y() < rock.get_position().get_y() + 10):
                print("hit a ROCK!!!")
                self.score -= 1
                rock.move_next(max_x, 1)



    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_points(self.score)
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()