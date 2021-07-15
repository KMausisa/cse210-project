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

        # Lists for Entities
        super().__init__()

        # Lists for Map Layers
        self.wall_list = None
        self.background_1_list = None
        self.background_2_list = None
        self.door_list = None
        self.door_list_2 = None
        self.switch_list = None
        self.switch_list_2 = None
        

        self.player_list = None
        self.player_sprite = None

        self.enemy = None
        self.enemy_list = None

        self.prize_list = None
        self.prize_fake_list = None
        self.door_list_1 = None
        self.door_list_2 = None
        self.button_list_1 = None
        self.button_list_2 = None
        
        # Sets the mouse to be invisible when on the Window
        self.window.set_mouse_visible(False)
        
        #Number of times you hit a door
        self.count = 0

        #Total amount of Lives
        self.lives = 3

        #Our Physics Engine
        self.physics_engine_player = None
        self.physics_engine__player_2 = None
        self.physics_engine_enemy = None
        self.physics_engine_enemy_2 = None
        self.physics_engine_enemy_3 = None


        arcade.set_background_color(arcade.csscolor.SKY_BLUE)

    def setup(self):
        """Sets up the charcter,walls, and primitive sound. """

        # Viewport
        self.view_left = 0
        self.view_bottom = 0
        changed_viewport = True
        
        self.game_over = arcade.load_sound(constants.GAMEOVER_PATH)
        self.button_press = arcade.load_sound(constants.SECRET_PATH)

        self.player_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.prize_list = arcade.SpriteList()
        self.door_list_1 =arcade.SpriteList()
        self.door_list_2= arcade.SpriteList()
        self.button_list_1 = arcade.SpriteList()
        self.button_list_2 = arcade.SpriteList()
        
        # Call Enemy Class
        self.enemy = Enemy()
        self.enemy.center_x = constants.ENEMY_START_X
        self.enemy.center_y = constants.ENEMY_START_Y
        self.enemy_list.append(self.enemy)

        self.enemy_2 = Enemy()
        self.enemy_2.center_x = constants.ENEMY_START_X + 500
        self.enemy_2.center_y = constants.ENEMY_START_Y
        self.enemy_list.append(self.enemy_2)

        self.enemy_3 = Enemy()
        self.enemy_3.center_x = constants.ENEMY_START_X + 1300
        self.enemy_3.center_y = constants.ENEMY_START_Y + 600
        self.enemy_list.append(self.enemy_3)

        #Sounds
        self.jumping_noise = arcade.load_sound(constants.JUMPING_PATH)

        self.player_sprite = Player()
        self.player_sprite.center_x = constants.PLAYER_START_X
        self.player_sprite.center_y = constants.PLAYER_START_Y
        self.player_list.append(self.player_sprite)


        # Name of the layer in the file that has our platforms/walls
        platforms_layer_name = "Platforms"
        background_1_layer_name = "Background1"
        background_2_layer_name = "Background 2"
        door_1_name = "Door 1"
        door_2_name = "Door 2"
        door_3_name = "Trap Doors"
        switch_1_name = "Switch 1"
        switch_2_name = "Switch 2"
        switch_3_name = "Switch 3"
        fake_coin_name = "Fake Coin"
        real_coin_name = "Real Coin"

        # Read in tiled map
        my_map = arcade.tilemap.read_tmx(constants.MAP_PATH)

        # -- Background --
        self.background_1_list = arcade.tilemap.process_layer(map_object=my_map,
                                                            layer_name=background_1_layer_name,
                                                            scaling=constants.MAP_SCALING,
                                                            use_spatial_hash=True)

        self.background_2_list = arcade.tilemap.process_layer(map_object=my_map,
                                                            layer_name=background_2_layer_name,
                                                            scaling=constants.MAP_SCALING,
                                                            use_spatial_hash=True)
        # -- Platforms --
        self.wall_list = arcade.tilemap.process_layer(map_object=my_map,
                                                        layer_name=platforms_layer_name,
                                                        scaling=constants.MAP_SCALING,
                                                        use_spatial_hash=True)


        self.switch_list = arcade.tilemap.process_layer(map_object=my_map,
                                                            layer_name=switch_1_name,
                                                            scaling=constants.MAP_SCALING,
                                                            use_spatial_hash=True)

        self.switch_list_2 = arcade.tilemap.process_layer(map_object=my_map,
                                                            layer_name=switch_2_name,
                                                            scaling=constants.MAP_SCALING,
                                                            use_spatial_hash=True)

        self.switch_list_3 = arcade.tilemap.process_layer(map_object=my_map,
                                                            layer_name=switch_3_name,
                                                            scaling=constants.MAP_SCALING,
                                                            use_spatial_hash=True)
        
        self.door_list_1 = arcade.tilemap.process_layer(map_object=my_map,
                                                        layer_name=door_1_name,
                                                        scaling=constants.MAP_SCALING,
                                                        use_spatial_hash=True)

        self.door_list_2 = arcade.tilemap.process_layer(map_object=my_map,
                                                        layer_name=door_2_name,
                                                        scaling=constants.MAP_SCALING,
                                                        use_spatial_hash=True)
                                                        
        self.door_list_3 = arcade.tilemap.process_layer(map_object=my_map,
                                                        layer_name=door_3_name,
                                                        scaling=constants.MAP_SCALING,
                                                        use_spatial_hash=True)                                                

        self.prize_fake_list = arcade.tilemap.process_layer(map_object=my_map,
                                                            layer_name=fake_coin_name,
                                                            scaling=constants.MAP_SCALING,
                                                            use_spatial_hash=True)

        self.prize_list = arcade.tilemap.process_layer(map_object=my_map,
                                                            layer_name=real_coin_name,
                                                            scaling=constants.MAP_SCALING,
                                                            use_spatial_hash=True)                                                    

        # Add Button 1
        self.button = arcade.Sprite(constants.BUTTON_PATH, constants.BUTTON_SCALING)
        self.button.center_x = 196
        self.button.center_y = 305
        self.button_list_1.append(self.button)




        #Create Physics Engine
        
        self.physics_engine_player = arcade.PhysicsEnginePlatformer(self.player_sprite,self.wall_list,constants.GRAVITY)
        self.physics_engine_enemy = arcade.PhysicsEnginePlatformer(self.enemy,self.wall_list,constants.GRAVITY)
        self.physics_engine_enemy_2 = arcade.PhysicsEnginePlatformer(self.enemy_2,self.wall_list,constants.GRAVITY)
        self.physics_engine_enemy_3 = arcade.PhysicsEnginePlatformer(self.enemy_3,self.wall_list,constants.GRAVITY)
        self.physics_engine_enemy_4 = arcade.PhysicsEnginePlatformer(self.enemy_3,self.door_list_3, constants.GRAVITY)
        
        # self.physics_engine_door_1 = arcade.PhysicsEnginePlatformer(self.player_sprite,self.door_list_2,constants.GRAVITY)

        

    def on_draw(self):
        "Draw whatever is on the screen"

        arcade.start_render()

        #Draw Sprites

        self.background_1_list.draw()
        self.background_2_list.draw()
        self.wall_list.draw()
        self.player_list.draw()
        self.prize_fake_list.draw()
        self.prize_list.draw()
        self.door_list_1.draw()
        self.door_list_2.draw()
        self.door_list_3.draw()
        self.switch_list.draw()
        self.switch_list_2.draw()
        self.switch_list_3.draw()
        self.enemy_list.draw()

        #Draw Lives
        output = f"Lives: {self.lives}"
        arcade.draw_text(output, 
                        start_x=10 + self.view_left, 
                        start_y=500 + self.view_bottom, 
                        color=arcade.csscolor.BLACK, 
                        font_size=18)

    def on_key_press(self, key, modifiers):

        """Tracks the user input on the Keyboard  """


        if key == arcade.key.UP or key == arcade.key.W:
            if self.physics_engine_player.can_jump():
                self.player_sprite.change_y = constants.PLAYER_JUMP_SPEED
                arcade.play_sound(self.jumping_noise)
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = (constants.PLAYER_MOVEMENT_SPEED * -1 )
            self.lives
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
        self.physics_engine_enemy_2.update()
        self.physics_engine_enemy_3.update()
        

        # enemy sprite will follow the player sprite
        for enemy in self.enemy_list:
            enemy.follow_sprite(self.player_sprite)
        

        # update player
        self.player_list.update_animation(delta_time)
        
        # Update enemy animation
        self.enemy_list.update_animation(delta_time)

        #Move Enemy with physics engine
        self.physics_engine_enemy.update()

        #Check if Enemy collides with Player

        if self.player_sprite.collides_with_list(self.enemy_list):
            self.lives -= 1
            arcade.play_sound(self.game_over)
            self.player_sprite.center_x = constants.PLAYER_START_X
            self.player_sprite.center_y = constants.PLAYER_START_Y
        
        # Check if fake coin collides with Player
        if self.player_sprite.collides_with_list(self.prize_fake_list):
            self.lives -= 1
            arcade.play_sound(self.game_over)
            self.player_sprite.center_x = constants.PLAYER_START_X
            self.player_sprite.center_y = constants.PLAYER_START_Y

        # self.prize_list.update()

        # Generate a list of all sprites that collided with the player.
        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.prize_list)

        # Loop through each colliding sprite, remove it, and add to the score.

        for coin in coins_hit_list:
            coin.remove_from_sprite_lists()
            view = WinnerView()
            self.window.show_view(view)
            self.player_sprite.center_x = constants.PLAYER_START_X
            self.player_sprite.center_y = constants.PLAYER_START_Y

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
        elif self.player_sprite.collides_with_list(self.door_list_3):
            self.lives -= 1
            arcade.play_sound(self.game_over)
            self.player_sprite.center_x = constants.PLAYER_START_X
            self.player_sprite.center_y = constants.PLAYER_START_Y


        if self.lives == 0:
            self.player_sprite.center_x = constants.PLAYER_START_X
            self.player_sprite.center_y = constants.PLAYER_START_Y
        
            view = GameOverView()
            self.window.show_view(view)

        # # Generate a list of all sprites that collided with the player.
        button_1_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.switch_list)
        button_2_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.switch_list_2)
        button_3_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.switch_list_3)



        if button_1_hit_list:
        # Loop through each colliding sprite, remove it, and add to the score.
            for door in self.door_list_1:
                arcade.play_sound(self.button_press)
                door.remove_from_sprite_lists()

            # self.prize_list.append(self.prize)

        elif button_2_hit_list:
            for door in self.door_list_2:
                arcade.play_sound(self.button_press)
                door.remove_from_sprite_lists()
        
        elif button_3_hit_list:
            for door in self.door_list_3:
                arcade.play_sound(self.button_press)
                door.remove_from_sprite_lists()

        
        # Manage Scrolling

        #Track if we need to change viewport

        changed = False

        # Scroll left
        left_boundary = self.view_left + constants.LEFT_VIEWPORT_MARGIN
        if self.player_sprite.left < left_boundary:
            self.view_left -= left_boundary - self.player_sprite.left
            changed = True

        #Scroll Right
        right_boundary = self.view_left + constants.SCREEN_WIDTH - constants.RIGHT_VIEWPORT_MARGIN
        if self.player_sprite.right > right_boundary:
            self.view_left += self.player_sprite.right - right_boundary
            changed = True

        #Scroll Up
        top_boundary = self.view_bottom + constants.SCREEN_HEIGHT - constants.TOP_VIEWPORT_MARGIN
        if self.player_sprite.top > top_boundary:
            self.view_bottom += self.player_sprite.top - top_boundary
            changed = True

        # Scroll down
        bottom_boundary = self.view_bottom + constants.BOTTOM_VIEWPORT_MARGIN
        if self.player_sprite.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player_sprite.bottom
            changed = True

        if changed:
            #Only scroll to integers. Otherwise we end up with pixels that are not lined up
            self.view_bottom = int(self.view_bottom)
            self.view_left = int(self.view_left)

            #Do Scrolling
            arcade.set_viewport(self.view_left,
                                constants.SCREEN_WIDTH + self.view_left,
                                self.view_bottom,
                                constants.SCREEN_HEIGHT + self.view_bottom)

            # self.lives.change_x = self.view_left











        


