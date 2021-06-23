import arcade
from game import constants


class Jungle(arcade.Window):
    "Main Application Class"

    def __init__(self):

        super().__init__(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)


        self.player_list = None
        self.wall_list = None

        arcade.set_background_color(arcade.csscolor.GOLD)

    def setup(self):

        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        image = ":resources:images/animated_characters/male_adventurer/maleAdventurer_idle.png"
        self.player_sprite = arcade.Sprite(image, constants.CHARACTER_SCALING)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 100
        self.player_list.append(self.player_sprite)


        #Add Wall

        for x in (0, 1000, 50):
            ground_image = ":resources:images/tiles/stone.png" 
            wall =arcade.Sprite(ground_image)
            wall.center_x = 0
            wall.center_y = 32
            self.wall_list.append(wall)
        


    def on_draw(self):
        "Draw whatever is on the screen"

        arcade.start_render()

        #Draw Sprites

        self.player_list.draw()
        self.wall_list.draw()


    def on_key_press(self):
        pass

    def on_key_release(self):
        pass
