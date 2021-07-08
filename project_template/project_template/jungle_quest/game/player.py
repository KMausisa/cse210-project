import arcade
from game import constants

class Player(arcade.Sprite):

    def __init__(self):

        pass

    def create_player(self, player_list):
        image = ":resources:images/animated_characters/male_adventurer/maleAdventurer_idle.png"
        self.player_sprite = arcade.Sprite(image, constants.CHARACTER_SCALING)
        self.player_sprite.center_x = constants.PLAYER_START_X
        self.player_sprite.center_y = constants.PLAYER_START_Y
        
        return player_list.append(self.player_sprite)