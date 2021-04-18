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
GREEN = ("#97E067")  # 1 - Straight/Flat/Solid
BROWN = ("#775D44")  # 2 - Mountain
BLUE = ("#54C2EA")  # 3 - Swamp
RED = ("#C95E52")  # 4 - Fire
WHITE = ("#FFFFFF")  # Initial position color
BLACK = ("#000000")  # Final position color
ORANGE = ("#FFA500")  # Menu button normal state
LIGHT_ORANGE = ("#FF8D19")  # Menu button mouse hover
LIGHT_BLACK = ("#200E0E")  # Menu background
PURPLE = (128, 0, 128)
YELLOW = (255, 255, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)


def QuitGame():
    pygame.quit()
    sys.exit()
