import os

# Gets absolute Path
PATH = os.path.dirname(os.path.abspath(__file__))

#Establish Constants in the game

#Length and Width of Play screen
SCREEN_WIDTH = 720
SCREEN_HEIGHT= 540
SCREEN_TITLE = "Jungle Quest"

#Size of Ground and of Character
CHARACTER_SCALING = 1.5
MAP_SCALING = 2
TITLE_SCALING = 1

# Player image
PLAYER_IMG_TEST = os.path.join(PATH, '..', 'assets', 'kenney_pixelplatformer', 'Characters', 'character_0000.png')

# Tiled Map
MAP_PATH = os.path.join(PATH, '..', 'assets', 'project-map-2.tmx')

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


# -- Enemy --

# Enemy Path
ENEMY_PATH = os.path.join(PATH, '..', 'assets', 'kenney_pixelplatformer', 'Characters', 'character_0015.png')

#Size of enemy 
ENEMY_SIZE = 1.5

# Where the first enemy will start
ENEMY_START_X = 512
ENEMY_START_Y = 256

# How fast the enemy will move
ENEMY_MOVEMENT_SPEED = 1


# -- Button

# Button path
BUTTON_PATH = os.path.join(PATH, '..', 'assets', 'kenney_pixelplatformer', 'Tiles', 'tile_0064.png')

#Button Size
BUTTON_SCALING = 2


# -- Door --

# Door Path
DOOR_PATH = os.path.join(PATH, '..', 'assets', 'kenney_pixelplatformer', 'Tiles', 'tile_0130.png')

#Door Size
DOOR_SCALING = 2

# -- SWITCH --

# Switch Path
SWITCH_PATH = os.path.join(PATH, '..', 'assets', 'kenney_pixelplatformer', 'Tiles', 'tile_0064.png')


# -- Coin --

# Coin Path
COIN_PATH = os.path.join(PATH, '..', 'assets', 'kenney_pixelplatformer', 'Tiles', 'tile_0151.png')

# Viewport
LEFT_VIEWPORT_MARGIN = 250
RIGHT_VIEWPORT_MARGIN = 250
BOTTOM_VIEWPORT_MARGIN = 50
TOP_VIEWPORT_MARGIN = 100



