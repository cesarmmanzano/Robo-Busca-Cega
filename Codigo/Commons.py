import pygame
import sys

# Game constants
GAME_WIDTH = 798
GAME_ROWS = 42
SQUARE_SIZE = GAME_WIDTH // GAME_ROWS

GAME_TITLE = "Robo Busca Cega"
FILE_NAME = None # Will be set when user chooses a file
CHOOSE_A_FILE = "Escolha o arquivo"
# Font to be used
HELVETICA_NEUE_FONT = "Helvetica Neue"

# To control which algorithm will be used
A_ALGORITHM = "A* Algorithm"
BLIND_SEARCH_ALGORITHM = "Blind Search Algorithm"
global CurrentAlgorithm

# Menu strings
NAMES_TITLE = "Cesar Marrote Manzano & Victor Felipe dos Santos"
BUTTON_2_TEXT = "Blind Search"
INSTRUCTIONS_TITLE = "Instruções: "
INSTRUCTIONS_TITLE0_MENU = "Primeiro selecione o arquivo que deseja utilizar"
INSTRUCTIONS_TITLE1_MENU = "Ao entrar na tela aperte espaço ou enter do teclado numérico para iniciar"
INSTRUCTIONS_TITLE2_MENU = "Ao terminar o algoritmo pressione 'r' para reiniciar"
INSTRUCTIONS_TITLE3_MENU = "Você pode pressionar ESC a qualquer momento para fechar a janela"

# Game info strings
VISITED_NODES = "Nós visitados: "
PATH_TOTAL_WEIGHT = "Custo do caminho: "

# Hex Colors
LIGHT_GREEN = ("#97E067")  # 1 - Straight/Flat/Solid
LIGHT_BROWN = ("#775D44")  # 2 - Mountain
LIGHT_BLUE = ("#54C2EA")  # 3 - Swamp
LIGHT_RED = ("#C95E52")  # 4 - Fire
BLACK = ("#000000") # Border and main button text color
WHITE = ("#FFFFFF") # Secondary text color
ORANGE = ("#FFA500") # Normal state menu button color
LIGHT_ORANGE = ("#FF8D19") # Hover state menu button color
LIGHT_BLACK = ("#200E0E") # Background menu color
YELLOW = ("#FFFF00") # Path color
GREEN = ("#009900") # Initial position color
RED = ("#FF0000") # Final position color

def QuitGame():
    pygame.quit()
    sys.exit()

def RenderText(window, stringToRender, rect, fontSize = 15, color = WHITE):
    pygame.font.init()
    myfont = pygame.font.SysFont(HELVETICA_NEUE_FONT, fontSize)
    string = myfont.render(stringToRender, True, color)
    window.blit(string, rect)    