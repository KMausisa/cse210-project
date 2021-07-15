import arcade
from game import constants
from game.jungle import Jungle

class InstructionView(arcade.View):
    """A class that defines the starting window or the window the user will first see.
    It will display the name of the game, how to start the game, and the instructions for how to play.
    """
    def __init__(self):
        """Class constructor. This class loads the textures/images for the window.
        """
        super().__init__()
        # Load background music
        self.background_music = arcade.load_sound(constants.MUSIC_PATH)
        arcade.play_sound(sound=self.background_music, volume=0.25)

        # Load player image
        self.player_image = arcade.load_texture(constants.PLAYER_IMG_TEST)

        # Load enemy image
        self.enemy_image = arcade.load_texture(constants.ENEMY_PATH)


        # Load coin image
        self.coin_image = arcade.load_texture(constants.COIN_PATH)

        # Load door image
        self.door_image = arcade.load_texture(constants.DOOR_PATH)

        # Load switch image
        self.switch_image = arcade.load_texture(constants.SWITCH_PATH)



    def on_show(self):
        """ This is run once when we switch to this view """
        arcade.set_background_color(arcade.csscolor.BLACK)

        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        arcade.set_viewport(0, constants.SCREEN_WIDTH - 1, 0, constants.SCREEN_HEIGHT - 1)


    def on_draw(self):
        """ Draw this view """
        arcade.start_render()

        # Display the Name of the game
        arcade.draw_text(text="Jungle Quest", start_x=constants.SCREEN_WIDTH / 2, start_y=(constants.SCREEN_HEIGHT - 150), 
                        color=arcade.color.WHITE, font_size=50, anchor_x="center")
        
        # Display the user input to start the game
        arcade.draw_text(text="Click to advance", start_x=constants.SCREEN_WIDTH / 2, start_y=(constants.SCREEN_HEIGHT - 200), 
                        color=arcade.color.WHITE, font_size=20, anchor_x="center")

        # -- PLAYER --

        # Draw the player the user will control
        self.player_image.draw_sized(center_x=250, center_y=(constants.SCREEN_HEIGHT - 300), 
                                    width=36, height=36)

        # Description of the player
        arcade.draw_text(text="Playable Adventurer", start_x=430, start_y=(constants.SCREEN_HEIGHT - 315), 
                        color=arcade.color.WHITE, font_size=15, anchor_x="center")

        # -- ENEMY --

        # Draw the enemy the user will have to avoid
        self.enemy_image.draw_sized(center_x=250, center_y=(constants.SCREEN_HEIGHT - 350), 
                                    width=36, height=36)

        # Description of the enemy
        arcade.draw_text(text="Wandering Enemies. They will kill you!", start_x=430, start_y=(constants.SCREEN_HEIGHT - 365), 
                        color=arcade.color.WHITE, font_size=15, anchor_x="center")

        # -- COIN -- 

        # Draw the coin the user will have to get 
        self.coin_image.draw_sized(center_x=250, center_y=(constants.SCREEN_HEIGHT - 405), 
                                width=36, height=36)

        # Description of the coin
        arcade.draw_text(text="Get the prize to win the game!\nCareful! There is a fake prize!", 
                            start_x=430, start_y=(constants.SCREEN_HEIGHT - 420), 
                            color=arcade.color.WHITE, font_size=15, 
                            align="center", anchor_x="center")


        # -- DOOR --

        # Draw the door the user has to open
        self.door_image.draw_sized(center_x=230, center_y=(constants.SCREEN_HEIGHT - 455), 
                                    width=36, height=36)

        # Description of the door
        arcade.draw_text(text="This is the door. Hit the switch to\nget through it. It can hurt you.", 
                            start_x=430, start_y=(constants.SCREEN_HEIGHT - 475), 
                            color=arcade.color.WHITE, font_size=15, 
                            align="center", anchor_x="center")

        # -- SWITCH --

        # Draw the switch the user has to use to open
        self.switch_image.draw_sized(center_x=280, center_y=(constants.SCREEN_HEIGHT - 455), 
                                        width=36, height=36)


        
        


    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ If the user presses the mouse button, start the game. """
        game_view = Jungle()
        game_view.setup()
        self.window.show_view(game_view)
