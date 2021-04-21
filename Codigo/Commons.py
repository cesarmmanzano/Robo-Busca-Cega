import pygame
import sys

# Game constants
GAME_WIDTH = 798
TUTORIAL_WIDTH = 20
GAME_ROWS = 42
SQUARE_SIZE = GAME_WIDTH // GAME_ROWS
GAME_TITLE = "Robo Busca Cega"
FILE_NAME = "Codigo/index.txt"

# Font to de used
HELVETICA_NEUE_FONT = "Helvetica Neue"

# To control which algorithm will be used
A_ALGORITHM = "A* Algorithm"
BLIND_SEARCH_ALGORITHM = "Blind Search Algorithm"
global currentAlgorithm

# Menu title
NAMES_TITLE = "Cesar Marrote Manzano & Victor Felipe dos Santos"
INSTRUCTIONS_TITLE = "Instruções: "
INSTRUCTIONS_TITLE1_MENU = "Ao entrar na tela aperte espaço para iniciar"
INSTRUCTIONS_TITLE2_MENU = "Ao terminar o algoritmo pressione 'r' para reiniciar"
INSTRUCTIONS_TITLE3_MENU = "Voce pode pressionar ESC para fechar a janela a qualquer momento"

# Hex Colors
GREEN = ("#97E067")  # 1 - Straight/Flat/Solid
BROWN = ("#775D44")  # 2 - Mountain
BLUE = ("#54C2EA")  # 3 - Swamp
RED = ("#C95E52")  # 4 - Fire
ORANGE = ("#FFA500")  # Menu button normal state
LIGHT_ORANGE = ("#FF8D19")  # Menu button mouse hover
LIGHT_BLACK = ("#200E0E")  # Menu background
YELLOW = ("#FFFF00") # Path color
START_POSITION_COLOR = ("#009900") # green for start position
FINAL_POSITION_COLOR = ("#FF0000") # red for final position
WHITE = ("#FFFFFF")
BLACK = ("#000000")
PURPLE = (128, 0, 128)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)


def QuitGame():
    pygame.quit()
    sys.exit()
