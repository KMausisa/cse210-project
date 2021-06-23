import arcade

SCREEN_WIDTH = 500
SCREEN_HEIGHT= 800
SCREEN_TITLE = "Jungle Quest"

class Jungle(arcade.Window):
    "Main Application Class"

    def __init__(self):

        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        arcade.set_background_color(arcade.csscolor.GOLD)

    def setup(self):

        pass


    def on_draw(self):
        "Draw whatever is on the screen"

        arcade.start_render()