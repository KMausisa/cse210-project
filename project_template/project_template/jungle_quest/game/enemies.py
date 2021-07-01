from game import constants
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
        self.enemy = None
        self.enemy_list = None

        self._setup()

    def _setup(self):
        """Creates the enemy sprites

        Args:
            self (Enemy): An instance of Enemy
        """
        self.enemy_list = arcade.SpriteList()
        enemy_image = ":resources:/images/enemies/slimeBlue.png"

        self.enemy = arcade.Sprite(enemy_image)
        self.enemy.textures = []

        # Append textures to the list
        # self.enemy.textures.append(arcade.load_texture(enemy_image))
        # self.enemy.textures.append(arcade.load_texture(enemy_image, flipped_vertically=True))

        self.enemy.center_x = constants.ENEMY_START_X
        self.enemy.center_y = constants.ENEMY_START_Y
        
        self.enemy_list.append(self.enemy)

    def follow_sprite(self, player_sprite):
        """This function will move the current sprite towards whatever
        other sprite is specified as a parameter.

        We use the 'min' function here to get the sprite to line up with
        the target sprite, and not jump around if the sprite is not off
        an exact multiple of SPRITE_SPEED.
        """

        if self.enemy.center_x < player_sprite.center_x:
            self.enemy.center_x += min(constants.ENEMY_MOVEMENT_SPEED, player_sprite.center_x - self.enemy.center_x)
            # self.enemy.cur_texture_index = 0
        elif self.enemy.center_x > player_sprite.center_x:
            self.enemy.center_x -= min(constants.ENEMY_MOVEMENT_SPEED, self.enemy.center_x - player_sprite.center_x)
            # self.enemy.cur_texture_index = 1

    
