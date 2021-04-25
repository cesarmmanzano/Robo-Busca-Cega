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

# Menu strings
NAMES_TITLE = "Cesar Marrote Manzano & Victor Felipe dos Santos"
BUTTON_2_TEXT = "Blind Search"
INSTRUCTIONS_TITLE = "Instruções: "
INSTRUCTIONS_TITLE1_MENU = "Ao entrar na tela aperte espaço ou enter do teclado numérico para iniciar"
INSTRUCTIONS_TITLE2_MENU = "Ao terminar o algoritmo pressione 'r' para reiniciar"
INSTRUCTIONS_TITLE3_MENU = "Voce pode pressionar ESC para fechar a janela a qualquer momento"

# Game infos strings
VISITED_NODES = "Nós visitados: " 
PATH_TOTAL_WEIGHT = "Custo do caminho: "

# Hex Colors
GREEN = ("#97E067")  # 1 - Straight/Flat/Solid
BROWN = ("#775D44")  # 2 - Mountain
BLUE = ("#54C2EA")  # 3 - Swamp
RED = ("#C95E52")  # 4 - Fire
BLACK = ("#000000")
WHITE = ("#FFFFFF")
ORANGE = ("#FFA500")  # Menu button normal state
MENU_BUTTON_HOVER_COLOR = ("#FF8D19")  # Menu button mouse hover
BACKGROUND_MENU_COLOR = ("#200E0E")  # Menu background
PATH_COLOR = ("#FFFF00") # Path color
START_POSITION_COLOR = ("#009900") # green for start position
FINAL_POSITION_COLOR = ("#FF0000") # red for final position

def QuitGame():
    pygame.quit()
    sys.exit()
    
def RenderText(window, stringToRender, rect, fontSize = 15, color = WHITE):    
    pygame.font.init()
    myfont = pygame.font.SysFont(HELVETICA_NEUE_FONT, fontSize)
    string = myfont.render(stringToRender, True, color)
    window.blit(string, rect)
    