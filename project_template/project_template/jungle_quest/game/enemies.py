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
        
        self.scale = constants.ENEMY_SIZE
        
        # Load texture pair
        self.idle_texture_pair = load_texture_pair(constants.ENEMY_PATH)

        # set the initial texture
        self.texture = self.idle_texture_pair[0]
        

    def follow_sprite(self, player_sprite):
        """This function will move the current sprite towards whatever
        other sprite is specified as a parameter.

        We use the 'min' function here to get the sprite to line up with
        the target sprite, and not jump around if the sprite is not off
        an exact multiple of SPRITE_SPEED.
        """

        if self.center_x < player_sprite.center_x:
            self.center_x += min(constants.ENEMY_MOVEMENT_SPEED, player_sprite.center_x - self.center_x)
            # self.enemy.cur_texture_index = 0
        elif self.center_x > player_sprite.center_x:
            self.center_x -= min(constants.ENEMY_MOVEMENT_SPEED, self.center_x - player_sprite.center_x)
            # self.enemy.cur_texture_index = 1

    
