import arcade
from game import constants
from game.enemies import Enemy

class Jungle(arcade.Window):
    "Main Application Class"

    def __init__(self):

        super().__init__(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)


        self.player_list = None
        self.wall_list = None
        self.player_sprite = None
        self.enemy = None

        #Our Physics Engine
        self.physics_engine_player = None
        self.physics_engine_enemy = None

        arcade.set_background_color(arcade.csscolor.BLACK)

    def setup(self):
        """Sets up the charcter,walls, and primitive sound. """

        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.enemy = Enemy()

        #Sounds
        self.jumping_noise = arcade.load_sound(":resources:sounds/jump2.wav")

        image = ":resources:images/animated_characters/male_adventurer/maleAdventurer_idle.png"
        self.player_sprite = arcade.Sprite(image, constants.CHARACTER_SCALING)
        self.player_sprite.center_x = constants.PLAYER_START_X
        self.player_sprite.center_y = constants.PLAYER_START_Y
        self.player_list.append(self.player_sprite)


        #Add Wall

        for x in range(0, 1250, 64):
            ground_image = ":resources:images/tiles/stone.png" 
            wall = arcade.Sprite(ground_image, constants.TITLE_SCALING)
            wall.center_x = x
            wall.center_y = 32
            self.wall_list.append(wall)

        #Create Physics Engine
        self.physics_engine_player = arcade.PhysicsEnginePlatformer(self.player_sprite, self.wall_list,constants.GRAVITY)
        self.physics_engine_enemy = arcade.PhysicsEnginePlatformer(self.enemy.enemy, self.wall_list, constants.GRAVITY)

    def on_draw(self):
        "Draw whatever is on the screen"

        arcade.start_render()

        #Draw Sprites

        self.player_list.draw()
        self.wall_list.draw()
        self.enemy.enemy_list.draw()


    def on_key_press(self, key, modifiers):

        """Tracks the user input on the Keyboard  """


        if key == arcade.key.UP or key == arcade.key.W:
            if self.physics_engine_player.can_jump():

                self.player_sprite.change_y = constants.PLAYER_JUMP_SPEED
                # arcade.play_sound(self.jumping_noise)
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = (constants.PLAYER_MOVEMENT_SPEED * -1 )
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = constants.PLAYER_MOVEMENT_SPEED



    def on_key_release(self, key, modifiers):
        """Stops the player character from moving when keyboard is not pressed  """

        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """Movement and game logic"""

        # Move the player with the physics engine
        self.physics_engine_player.update()
        self.physics_engine_enemy.update()

        # enemy sprite will follow the player sprite
        self.enemy.follow_sprite(self.player_sprite)

        
        # Checks for collision with enemies
        if self.player_sprite.collides_with_list(self.enemy.enemy_list):
            # if self.player_sprite.center_y > (self.enemy.enemy.center_y + 64):
            #     self.enemy.remove_from_sprite_lists()
            # elif self.player_sprite.center_y < (self.enemy.enemy.center_y + 64):
            arcade.close_window()




