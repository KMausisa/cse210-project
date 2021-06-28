import arcade
from game import constants
from game.player import Player


class Jungle(arcade.Window):
    "Main Application Class"

    def __init__(self):

        super().__init__(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)

        #self.player = Player()
        self.player_list = None
        self.player_sprite = None
        self.wall_list = None
        self.prize_list = None
        self.enemy_list = None
        


        #Our Physics Engine
        self.physics_engine = None

        arcade.set_background_color(arcade.csscolor.BLACK)

    def setup(self):
        """Sets up the charcter,walls, and primitive sound. """

        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.prize_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()

        #Sounds
        self.jumping_noise = arcade.load_sound(":resources:sounds/jump2.wav")


        # self.player_list = self.player.create_player(self.player_list, self.player_sprite)

        image = ":resources:images/animated_characters/male_adventurer/maleAdventurer_idle.png"
        self.player_sprite = arcade.Sprite(image, constants.CHARACTER_SCALING)
        self.player_sprite.center_x = constants.PLAYER_START_X
        self.player_sprite.center_y = constants.PLAYER_START_Y
        self.player_list.append(self.player_sprite)


        #Add Wall

        for x in range(0, 1250, 64):
            ground_image = ":resources:images/tiles/stone.png" 
            wall =arcade.Sprite(ground_image, constants.TITLE_SCALING)
            wall.center_x = x
            wall.center_y = 32
            self.wall_list.append(wall)


        #Add Prize
        image = ":resources:images/items/coinGold.png"
        prize = arcade.Sprite(image, constants.COIN_SCALING)
        prize.center_x = 800
        prize.center_y = 200
        self.prize_list.append(prize)

        #Set up Enemys
        enemy = arcade.Sprite(":resources:images/enemies/wormGreen.png", constants.ENEMY_SIZE)

        enemy.bottom = constants.ENEMY_SIZE
        enemy.left = constants.ENEMY_SIZE * 2

        # Set enemy initial speed
        enemy.change_x = 2
        self.enemy_list.append(enemy)

        # https://arcade.academy/examples/sprite_enemies_in_platformer.html#sprite-enemies-in-platformer
    


        #Create Physics Engine
        
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite,self.wall_list,constants.GRAVITY)

    def on_draw(self):
        "Draw whatever is on the screen"

        arcade.start_render()

        #Draw Sprites

        self.player_list.draw()
        self.wall_list.draw()
        self.prize_list.draw()
        self.enemy_list.draw()

    def on_key_press(self, key, modifiers):

        """Tracks the user input on the Keyboard  """


        if key == arcade.key.UP or key == arcade.key.W:
            if self.physics_engine.can_jump():

                self.player_sprite.change_y = constants.PLAYER_JUMP_SPEED
                arcade.play_sound(self.jumping_noise)
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
        self.physics_engine.update()


