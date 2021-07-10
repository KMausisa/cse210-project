import arcade
from game import constants
from game.jungle import Jungle

class InstructionView(arcade.View):

    def __init__(self):
        super().__init__()
        self.player_image = arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_idle.png")

        self.enemy_image = arcade.load_texture(":resources:/images/enemies/slimeBlue.png")

        self.background_music = arcade.load_sound(
        ":resources:music/1918.mp3"
        )

        self.coin_image = arcade.load_texture(":resources:images/items/coinGold.png")

        self.door_image = arcade.load_texture(":resources:images/tiles/doorClosed_mid.png")

        self.switch_image = arcade.load_texture(":resources:images/tiles/switchRed_pressed.png")

        arcade.play_sound(self.background_music)


    def on_show(self):
        """ This is run once when we switch to this view """
        arcade.set_background_color(arcade.csscolor.BLACK)

        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        arcade.set_viewport(0, constants.SCREEN_WIDTH - 1, 0, constants.SCREEN_HEIGHT - 1)


    def on_draw(self):
        """ Draw this view """
        arcade.start_render()
        arcade.draw_text("Jungle Quest", constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2, arcade.color.WHITE, font_size=50, anchor_x="center")
        
        arcade.draw_text("Click to advance", constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2-75, arcade.color.WHITE, font_size=20, anchor_x="center")

        self.player_image.draw_sized(300, constants.SCREEN_HEIGHT / 2-125, 50, 75)

        arcade.draw_text("Playable Adventurer", 430, constants.SCREEN_HEIGHT / 2-150, arcade.color.WHITE, font_size=15, anchor_x="center")

        self.enemy_image.draw_sized(300, constants.SCREEN_HEIGHT / 2-175, 60, 75)

        arcade.draw_text("Wandering Enemies. They will kill you!", 500, constants.SCREEN_HEIGHT / 2-210, arcade.color.WHITE, font_size=15, anchor_x="center")

        self.coin_image.draw_sized(300, constants.SCREEN_HEIGHT / 2-250, 90, 75)

        arcade.draw_text("Get the prize to win the game!  Careful! There is a flase Prize!", 585, constants.SCREEN_HEIGHT / 2-260, arcade.color.WHITE, font_size=15, anchor_x="center")

        self.door_image.draw_sized(300, constants.SCREEN_HEIGHT / 2-310, 50, 50)

        arcade.draw_text("This is the door. Hit the switch to get through it.  It can hurt you.", 595, constants.SCREEN_HEIGHT / 2-315, arcade.color.WHITE, font_size=15, anchor_x="center")

        self.switch_image.draw_sized(300, constants.SCREEN_HEIGHT / 2-355, 50, 60)

        arcade.draw_text("Hit this switch to open the door.", 595, constants.SCREEN_HEIGHT / 2-375, arcade.color.WHITE, font_size=15, anchor_x="center")


        
        


    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ If the user presses the mouse button, start the game. """
        game_view = Jungle()
        game_view.setup()
        self.window.show_view(game_view)
