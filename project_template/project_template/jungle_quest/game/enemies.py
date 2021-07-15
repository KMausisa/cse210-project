from game import constants
from game.load_texture_pair import load_texture_pair
import arcade

class Enemy(arcade.Sprite):
    """Enemmy that tries to stop the player.
    """
    def __init__(self):
        """Class constructor.

        Args:
            self (Enemy): An instance of Enemy.
        """
        super().__init__()
        
        # Default to face right
        self.character_face_direction = constants.LEFT_FACING

        # Used for flipping between image sequences
        self.cur_texture = 0
        self.scale = constants.ENEMY_SIZE
        
        # Load texture pair
        self.idle_texture_pair = load_texture_pair(constants.ENEMY_PATH)

        # set the initial texture
        self.texture = self.idle_texture_pair[self.character_face_direction]
        

    def follow_sprite(self, player_sprite):
        """This function will move the current sprite towards whatever
        other sprite is specified as a parameter.

        We use the 'min' function here to get the sprite to line up with
        the target sprite, and not jump around if the sprite is not off
        an exact multiple of SPRITE_SPEED.
        """

        if self.center_x < player_sprite.center_x:
            # self.center_x += min(constants.ENEMY_MOVEMENT_SPEED, player_sprite.center_x - self.center_x)
            self.change_x = constants.ENEMY_MOVEMENT_SPEED
        elif self.center_x > player_sprite.center_x:
            # self.center_x -= min(constants.ENEMY_MOVEMENT_SPEED, self.center_x - player_sprite.center_x)
            self.change_x = constants.ENEMY_MOVEMENT_SPEED * -1
        
        elif self.center_x == player_sprite.center_x:
            self.change_x = 0

            
    
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
            
        self.texture = self.idle_texture_pair[self.character_face_direction]

    
