import arcade
from game import constants
from game.load_texture_pair import load_texture_pair

class Player(arcade.Sprite):

    def __init__(self):
        """The class constructor for the player class.

        Args:
            self (Player): An instance of Player.
        """

        super().__init__()

        # Default to face right
        self.character_face_direction = constants.RIGHT_FACING

        # Used for flipping between image sequences
        self.cur_texture = 0
        self.scale = constants.CHARACTER_SCALING

        # Load texture pair
        self.idle_texture_pair = load_texture_pair(constants.PLAYER_IMG_TEST)

        # set the initial texture
        self.texture = self.idle_texture_pair[1]

        def update_animation(self, delta_time: float = 1/60):
            """Creating character animation

            Args:
                self (Player): An instance of Player.
                delta_time (float): The time it takes to update the Player image
            """
            # Figure out if we need to flip face left or right
            if self.change_x < 0 and self.character_face_direction == constants.RIGHT_FACING:
                self.character_face_direction = constants.LEFT_FACING
            elif self.change_x > 0 and self.character_face_direction == constants.LEFT_FACING:
                self.character_face_direction = constants.RIGHT_FACING
            
            # Idle animation
            if self.change_x == 0:
                self.texture = self.idle_texture_pair[self.character_face_direction]
                return

            