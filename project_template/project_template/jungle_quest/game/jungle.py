import arcade
from game import constants
from game.player import Player
from game.enemies import Enemy

# SPRITE_SCALING = 0.5
# SPRITE_NATIVE_SIZE = 128
# SPRITE_SIZE = int(SPRITE_NATIVE_SIZE * SPRITE_SCALING)

class Jungle(arcade.Window):
    "Main Application Class"

    def __init__(self):

        super().__init__(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
        #self.player = Player()
        self.player_list = None
        self.player_sprite = None
        self.wall_list = None
        self.prize_list = None
        self.door_list_1 = None
        self.door_list_2 = None
        self.button_list_1 = None
        self.button_list_2 = None
        self.enemy = None
        
        #Number of times you hit a door
        self.count = 0

        #Total amount of Lives
        self.lives = 3

        #Our Physics Engine
        self.physics_engine = None
        self.physics_engine_enemy = None
        # self.physics_engine_door_1 = None

        arcade.set_background_color(arcade.csscolor.BLACK)

    def setup(self):
        """Sets up the charcter,walls, and primitive sound. """

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



        #Add Platform
        for x in range(64 * 3, 64 * 5, 64):
            wall = arcade.Sprite(":resources:images/tiles/stone.png",0.5)

            wall.center_x = 600
            wall.center_y = 200
            self.wall_list.append(wall)


        #Add Prize
        image = ":resources:images/items/coinGold.png"
        prize = arcade.Sprite(image, constants.COIN_SCALING)
        prize.center_x = 950
        prize.center_y = 175
        self.prize_list.append(prize)


        for i in range(2):
            door = arcade.Sprite(":resources:images/tiles/doorClosed_mid.png",
                                    constants.DOOR_SCALING)
            if self.count != 1:

                # Position Door
                door.center_x = 800
                door.center_y = 175

                # Add Door 1 to the lists
                self.door_list_1.append(door)
                self.count += 1
            else:
                #Position Door
                door.center_x = 400
                door.center_y = 175

                # Add the Door 2 to the lists
                self.door_list_2.append(door)



        #Add Button 1
        button_image = ":resources:images/tiles/switchRed_pressed.png" 
        button =arcade.Sprite(button_image, constants.BUTTON_SCALING)
        button.center_x = 600
        button.center_y = 255
        self.button_list_1.append(button)

        #Add Button 2
        button_image = ":resources:images/tiles/switchGreen_pressed.png" 
        button =arcade.Sprite(button_image, constants.BUTTON_SCALING)
        button.center_x = 200
        button.center_y = 125
        self.button_list_2.append(button)


        #Create Physics Engine
        
        self.physics_engine_player = arcade.PhysicsEnginePlatformer(self.player_sprite,self.wall_list,constants.GRAVITY)
        self.physics_engine_enemy = arcade.PhysicsEnginePlatformer(self.enemy.enemy,self.wall_list,constants.GRAVITY)
        # self.physics_engine_door_1 = arcade.PhysicsEnginePlatformer(self.player_sprite,self.door_list_2,constants.GRAVITY)

        

    def on_draw(self):
        "Draw whatever is on the screen"

        arcade.start_render()

        #Draw Sprites

        self.player_list.draw()
        self.wall_list.draw()
        self.prize_list.draw()
        self.door_list_1.draw()
        self.door_list_2.draw()
        self.button_list_1.draw()
        self.button_list_2.draw()
        self.enemy.enemy_list.draw()

        #Draw Lives
        output = f"Lives: {self.lives}"
        arcade.draw_text(output, 10, 750, arcade.color.WHITE, 25)

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



        #Move Enemy with physics engine
        self.physics_engine_enemy.update()

        # self.physics_engine_door_1.update()

        self.enemy.follow_sprite(self.player_sprite)
        #Update Doors
        self.door_list_1.update()
        self.door_list_2.update()


        #Check if Enemy collides with Player
        if self.player_sprite.collides_with_list(self.enemy.enemy_list):
            self.lives -= 1
            self.player_sprite.center_x = constants.PLAYER_START_X
            self.player_sprite.center_y = constants.PLAYER_START_Y

        

        self.prize_list.update()

        # Generate a list of all sprites that collided with the player.
        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.prize_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for coin in coins_hit_list:
            coin.remove_from_sprite_lists()
            arcade.close_window()

        # Generate a list of all sprites that collided with the player.
        if self.player_sprite.collides_with_list(self.door_list_1):
            self.lives -= 1
            self.player_sprite.center_x = constants.PLAYER_START_X
            self.player_sprite.center_y = constants.PLAYER_START_Y
        elif self.player_sprite.collides_with_list(self.door_list_2):
            self.lives -= 1
            self.player_sprite.center_x = constants.PLAYER_START_X
            self.player_sprite.center_y = constants.PLAYER_START_Y


        if self.lives == 0:
            arcade.close_window()

        # Generate a list of all sprites that collided with the player.
        button_1_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.button_list_1)
        button_2_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.button_list_2)



        if button_1_hit_list:
        # Loop through each colliding sprite, remove it, and add to the score.
            for door in self.door_list_1:
                door.remove_from_sprite_lists()
        elif button_2_hit_list:
            for door in self.door_list_2:
                door.remove_from_sprite_lists()


        


