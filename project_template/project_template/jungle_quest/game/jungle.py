import arcade
from game import constants
from game.player import Player
from game.enemies import Enemy
from game.game_over_window import GameOverView
from game.winner_window import WinnerView

# SPRITE_SCALING = 0.5
# SPRITE_NATIVE_SIZE = 128
# SPRITE_SIZE = int(SPRITE_NATIVE_SIZE * SPRITE_SCALING)

class Jungle(arcade.View):
    "Main Application Class"

    def __init__(self):

        # Lists for Map Layers
        self.wall_list = None
        self.background_1_list = None
        self.background_2_list = None

        # Lists for Entities
        super().__init__()
        #self.player = Player()

        self.player_list = None
        self.player_sprite = None
        self.prize_list = None
        self.door_list_1 = None
        self.door_list_2 = None
        self.button_list_1 = None
        self.button_list_2 = None
        self.enemy = None
        
        self.window.set_mouse_visible(False)
        
        #Number of times you hit a door
        self.count = 0

        #Total amount of Lives
        self.lives = 3

        #Our Physics Engine
        self.physics_engine = None
        self.physics_engine_enemy = None
        # self.physics_engine_door_1 = None

        arcade.set_background_color(arcade.csscolor.SKY_BLUE)

    def setup(self):
        """Sets up the charcter,walls, and primitive sound. """

        #Set up background music
        # self.background_music = arcade.load_sound(
        # ":resources:music/1918.mp3"
        # )

        # arcade.play_sound(self.background_music)
        
        self.game_over = arcade.load_sound(":resources:sounds/gameover3.wav")
        self.button_press = arcade.load_sound(":resources:sounds/secret2.wav")

        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.prize_list = arcade.SpriteList()
        self.door_list_1 =arcade.SpriteList()
        self.door_list_2= arcade.SpriteList()
        self.button_list_1 = arcade.SpriteList()
        self.button_list_2 = arcade.SpriteList()
        
        #Call Enemy Class
        self.enemy = Enemy()

        #Sounds
        self.jumping_noise = arcade.load_sound(":resources:sounds/jump2.wav")


        # self.player_list = self.player.create_player(self.player_list, self.player_sprite)

        image = ":resources:images/animated_characters/male_adventurer/maleAdventurer_idle.png"
        self.player_sprite = Player()
        self.player_sprite.center_x = constants.PLAYER_START_X
        self.player_sprite.center_y = constants.PLAYER_START_Y
        self.player_list.append(self.player_sprite)


        # Name of the layer in the file that has our platforms/walls
        platforms_layer_name = "Platforms"
        background_1_layer_name = "Background 1"
        background_2_layer_name = "Background 2"

        # Read in tiled map
        my_map = arcade.tilemap.read_tmx(constants.MAP_PATH)


        # -- Platforms --
        self.wall_list = arcade.tilemap.process_layer(map_object=my_map,
                                                      layer_name=platforms_layer_name,
                                                      scaling=constants.MAP_SCALING,
                                                      use_spatial_hash=True)

        # -- Background --
        self.background_1_list = arcade.tilemap.process_layer(map_object=my_map,
                                                            layer_name=background_1_layer_name,
                                                            scaling=constants.MAP_SCALING,
                                                            use_spatial_hash=True)
        
        self.background_2_list = arcade.tilemap.process_layer(map_object=my_map,
                                                            layer_name=background_2_layer_name,
                                                            scaling=constants.MAP_SCALING,
                                                            use_spatial_hash=True)

        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite,
                                                             self.wall_list,
                                                             constants.GRAVITY)

        # --- Other Stuff


        # Add Prize
        image = ":resources:images/items/coinGold.png"
        self.prize = arcade.Sprite(image, constants.COIN_SCALING)
        self.prize.center_x = 690
        self.prize.center_y = 64


        # for i in range(2):
        self.door = arcade.Sprite(constants.DOOR_PATH, constants.DOOR_SCALING)
        #     if self.count != 1:

            # Position Door
        self.door.center_x = 700
        self.door.center_y = 54

        #         # Add Door 1 to the lists
        self.door_list_1.append(self.door)
        #         self.count += 1
        #     else:
        #         #Position Door
        #         door.center_x = 400
        #         door.center_y = 175

        #         # Add the Door 2 to the lists
        #         self.door_list_2.append(door)




        # Add Button 1
        self.button = arcade.Sprite(constants.BUTTON_PATH, constants.BUTTON_SCALING)
        self.button.center_x = 196
        self.button.center_y = 305
        self.button_list_1.append(self.button)

        # #Add Button 2
        # button_image = ":resources:images/tiles/switchGreen_pressed.png" 
        # button =arcade.Sprite(button_image, constants.BUTTON_SCALING)
        # button.center_x = 200
        # button.center_y = 125
        # self.button_list_2.append(button)

        #Add Button 1
        #button_image = ":resources:images/tiles/switchRed_pressed.png" 
        #button =arcade.Sprite(button_image, constants.BUTTON_SCALING)
        #button.center_x = 600
        #button.center_y = 255
        #self.button_list_1.append(button)
        #":resources:images/tiles/switchGreen_pressed.png"
        #Add Button 2
        #button_image = ":resources:images/tiles/switchRed_pressed.png" 
        #button =arcade.Sprite(button_image, constants.BUTTON_SCALING)
        #button.center_x = 200
        #button.center_y = 125
        #self.button_list_2.append(button)



        #Create Physics Engine
        
        self.physics_engine_player = arcade.PhysicsEnginePlatformer(self.player_sprite,self.wall_list,constants.GRAVITY)
        self.physics_engine_enemy = arcade.PhysicsEnginePlatformer(self.enemy.enemy,self.wall_list,constants.GRAVITY)
        # self.physics_engine_door_1 = arcade.PhysicsEnginePlatformer(self.player_sprite,self.door_list_2,constants.GRAVITY)

        

    def on_draw(self):
        "Draw whatever is on the screen"

        arcade.start_render()

        #Draw Sprites

        self.background_1_list.draw()
        self.background_2_list.draw()
        self.wall_list.draw()
        self.player_list.draw()
        self.prize_list.draw()
        self.door_list_1.draw()
        # self.door_list_2.draw()
        self.button_list_1.draw()
        # self.button_list_2.draw()
        # self.enemy.enemy_list.draw()

        #Draw Lives
        output = f"Lives: {self.lives}"
        arcade.draw_text(output, 10, 750, arcade.color.WHITE, 25)

        arcade.draw_text(text=f"Player Center X: {self.player_sprite.center_x}",
                         start_x=16,
                         start_y=16,
                         color=arcade.csscolor.WHITE)

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
        # self.enemy.follow_sprite(self.player_sprite)

        # update player
        self.player_list.update_animation(delta_time)

        
        # Checks for collision with enemies
        # if self.player_sprite.collides_with_list(self.enemy.enemy_list):
            # if self.player_sprite.center_y > (self.enemy.enemy.center_y + 64):
            #     self.enemy.remove_from_sprite_lists()
            # elif self.player_sprite.center_y < (self.enemy.enemy.center_y + 64):
            # arcade.close_window()



        #Move Enemy with physics engine
        self.physics_engine_enemy.update()

        # self.physics_engine_door_1.update()

        # self.enemy.follow_sprite(self.player_sprite)
        #Update Doors
        # self.door_list_1.update()
        # self.door_list_2.update()


        #Check if Enemy collides with Player

        if self.player_sprite.collides_with_list(self.enemy.enemy_list):
            self.lives -= 1
            arcade.play_sound(self.game_over)
            self.player_sprite.center_x = constants.PLAYER_START_X
            self.player_sprite.center_y = constants.PLAYER_START_Y
        

        # self.prize_list.update()

        # Generate a list of all sprites that collided with the player.
        # coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.prize_list)

        # Loop through each colliding sprite, remove it, and add to the score.

        for coin in coins_hit_list:
            coin.remove_from_sprite_lists()
            view = WinnerView()
            self.window.show_view(view)

        # Generate a list of all sprites that collided with the player.
        if self.player_sprite.collides_with_list(self.door_list_1):
            self.lives -= 1
            arcade.play_sound(self.game_over)
            self.player_sprite.center_x = constants.PLAYER_START_X
            self.player_sprite.center_y = constants.PLAYER_START_Y
        elif self.player_sprite.collides_with_list(self.door_list_2):
            self.lives -= 1
            arcade.play_sound(self.game_over)
            self.player_sprite.center_x = constants.PLAYER_START_X
            self.player_sprite.center_y = constants.PLAYER_START_Y


        if self.lives == 0:
    
            view = GameOverView()
            self.window.show_view(view)

        # # Generate a list of all sprites that collided with the player.
        button_1_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.button_list_1)
        # button_2_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.button_list_2)



        if button_1_hit_list:
        # Loop through each colliding sprite, remove it, and add to the score.
            for door in self.door_list_1:
                arcade.play_sound(self.button_press)
                door.remove_from_sprite_lists()

            self.prize_list.append(self.prize)

#         elif button_2_hit_list:
#             for door in self.door_list_2:
#                 arcade.play_sound(self.button_press)
#                 door.remove_from_sprite_lists()



        


