import os

# Gets the absolute path to the current file
PATH = os.path.dirname(os.path.abspath(__file__))
PLAYER_IMG_TEST = os.path.join(PATH, '..', 'assets', 'kenney_pixelplatformer', 'Characters', 'character_0000.png')

#Establish Constants in the game

#Length and Width of Play screen
SCREEN_WIDTH = 1000
SCREEN_HEIGHT= 800
SCREEN_TITLE = "Jungle Quest"

#Size of Ground and of Character
CHARACTER_SCALING = 1
TITLE_SCALING = 1

# Player image
PLAYER_IMG = "assets/kenney_pixelplatformer/Characters/character_0000.png"
PLAYER_IMG = "assets/kenney_pixelplatformer/Characters/character_0000.png"

#Where the Play will Start
PLAYER_START_X = 64
PLAYER_START_Y = 225

# How fast Character Moves
PLAYER_MOVEMENT_SPEED = 5
GRAVITY = .75
PLAYER_JUMP_SPEED = 20

# Where the player will face
RIGHT_FACING = 0
LEFT_FACING = 1

#Size of Prize
COIN_SCALING = 1

#Size of enemy 
ENEMY_SIZE = 1

#Button Size
BUTTON_SCALING = 0.5

#Door Size
DOOR_SCALING = 1.25

# Where the first enemy will start
ENEMY_START_X = 512
ENEMY_START_Y = 225

# How fast the enemy will move
ENEMY_MOVEMENT_SPEED = 1


