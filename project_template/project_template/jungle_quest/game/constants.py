import os

# Gets absolute Path
PATH = os.path.dirname(os.path.abspath(__file__))

#Establish Constants in the game

#Length and Width of Play screen
SCREEN_WIDTH = 720
SCREEN_HEIGHT= 540
SCREEN_TITLE = "Jungle Quest"

#Size of Ground and of Character
CHARACTER_SCALING = 2
MAP_SCALING = 2
TITLE_SCALING = 1

# Player image
PLAYER_IMG_TEST = os.path.join(PATH, '..', 'assets', 'kenney_pixelplatformer', 'Characters', 'character_0000.png')
# Tiled Map
MAP_PATH = os.path.join(PATH, '..', 'assets', 'project-map.tmx')

#Where the Play will Start
PLAYER_START_X = 64
PLAYER_START_Y = 64

# How fast Character Moves
PLAYER_MOVEMENT_SPEED = 5
GRAVITY = 1
PLAYER_JUMP_SPEED = 17

# Where the player will face
RIGHT_FACING = 1
LEFT_FACING = 0

#Size of Prize
COIN_SCALING = 0.4

#Size of enemy 
ENEMY_SIZE = 1

# Button path
BUTTON_PATH = os.path.join(PATH, '..', 'assets', 'kenney_pixelplatformer', 'Tiles', 'tile_0064.png')

#Button Size
BUTTON_SCALING = 2

# Door Path
DOOR_PATH = os.path.join(PATH, '..', 'assets', 'kenney_pixelplatformer', 'Tiles', 'tile_0130.png')

#Door Size
DOOR_SCALING = 2

# Where the first enemy will start
ENEMY_START_X = 128
ENEMY_START_Y = 256

# How fast the enemy will move
ENEMY_MOVEMENT_SPEED = 1


