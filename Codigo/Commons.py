import pygame
import sys
import math
from queue import PriorityQueue
from pygame.locals import *

# Game constants
GAME_WIDTH = 798
GAME_ROWS = 42
GAME_TITLE = "Robo Busca Cega"
FILE_NAME = 'Codigo/index.txt'

HELVETICA_NEUE_FONT = "Helvetica Neue"

# To control which algorithm will be used
A_ALGORITHM = "A* Algorithm"
BLIND_SEARCH_ALGORITHM = "Blind Search Algorithm"
global currentAlgorithm

NAMES_TITLE = "Cesar Marrote Manzano & Victor Felipe dos Santos"

# RGB Colors
GREEN = (151, 224, 103)  # 1 - Straight/Flat/Solid
BROWN = (119, 93, 68)  # 2 - Mountain
BLUE = (84, 194, 234)  # 3 - Swamp
RED = (201, 94, 82)  # 4 - Fire
WHITE = (255, 255, 255)  # Initial position color
BLACK = (0, 0, 0)  # Final position color
ORANGE = (255, 165, 0)  # Menu button normal state
LIGHT_ORANGE = (255, 141, 25)  # Menu button mouse hover
LIGHT_BLACK = (32, 14, 14)  # Menu background
PURPLE = (128, 0, 128)
YELLOW = (255, 255, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)


def QuitGame():
    pygame.quit()
    sys.exit()
