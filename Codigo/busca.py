import pygame
import sys
import math
from queue import PriorityQueue
from pygame.locals import *

GAME_WIDTH = 798
GAME_ROWS = 42
GAME_TITLE = "Robo Busca Cega"
FILE_NAME = 'Codigo/index.txt'

# To control which algorithm will be used
A_ALGORITHM = "A* Algorithm"
BLIND_SEARCH_ALGORITHM = "Blind Search Algorithm"
global currentAlgorithm

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

# ==================== #


class Spot:
    def __init__(self, col, row, width, color, weight):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = color
        self.neighbors = []
        self.width = width
        self.total_rows = GAME_ROWS
        self.weight = weight

    def GetWeight(self):
        return self.weight

    def IsStartPosition(self):
        return self.color == WHITE

    def IsEndPosition(self):
        return self.color == BLACK

    def ColorStartPosition(self):
        self.color = WHITE

    def ColorFinalPosition(self):
        self.color = BLACK

    def Draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.width))

    # the methods below are not used yet. Some of them will not be necessary
    def GetCurrentPosition(self):
        return self.row, self.col

    def IsClosed(self):
        return self.color == RED

    def IsOpen(self):
        return self.color == GREEN

    def Reset(self):
        self.color = WHITE

    def MakeClosed(self):
        self.color = RED

    def MakeOpen(self):
        self.color = GREEN

    def MakePath(self):
        self.color = PURPLE

    def CreateNeighbors(self, grid):
        self.neighbors = []

        # DOWN
        if self.row < self.total_rows - 1:
            self.neighbors.append(grid[self.row + 1][self.col])

        # UP
        if self.row > 0:
            self.neighbors.append(grid[self.row - 1][self.col])

        # RIGHT
        if self.col < self.total_rows - 1:
            self.neighbors.append(grid[self.row][self.col + 1])

        # LEFT
        if self.col > 0:
            self.neighbors.append(grid[self.row][self.col - 1])

    def __lt__(self, other):
        return False

# ==================== #


def ReadFile():

    with open(FILE_NAME, 'r') as f:
        ws, hs = [int(x) for x in next(f).split(',')]
        we, he = [int(x) for x in next(f).split(',')]
        startPosition = [ws, hs]
        finalPosition = [we, he]
        gameMap = [[int(num) for num in line.split(',')] for line in f]

    #result [ [start], [final], [map] ]
    result = []
    result.append(startPosition)
    result.append(finalPosition)
    result.append(gameMap)

    return result

# ==================== #


def DrawGrid(window):
    gap = GAME_WIDTH // GAME_ROWS
    for i in range(GAME_ROWS):
        pygame.draw.line(window, BLACK, (0, i * gap), (GAME_WIDTH, i * gap))
        for j in range(GAME_ROWS):
            pygame.draw.line(window, BLACK, (j * gap, 0), (j * gap, GAME_WIDTH))

# ==================== #


def Draw(window, grid):

    for row in grid:
        for spot in row:
            spot.Draw(window)

    DrawGrid(window)
    pygame.display.update()

# ==================== #


def BuildInitialWindow(grid):
    windowGrid = []
    gap = GAME_WIDTH // GAME_ROWS
    for i in range(GAME_ROWS):
        windowGrid.append([])
        for j in range(GAME_ROWS):

            if grid[i][j] == 1:
                color = GREEN
                weight = 1
            elif grid[i][j] == 2:
                color = BROWN
                weight = 5
            elif grid[i][j] == 3:
                color = BLUE
                weight = 10
            elif grid[i][j] == 4:
                color = RED
                weight = 15

            spot = Spot(i, j, gap, color, weight)
            windowGrid[i].append(spot)

    return windowGrid

# ==================== #


def MainMapScreen(window):

    isMenuRunning = False

    file = ReadFile()
    initialPosition = file[0]  # initialPosition[i, j]
    finalPosition = file[1]  # finalPosition[i, j]
    fileGrid = file[2]

    windowGrid = BuildInitialWindow(fileGrid)

    isGameRunning = True

    # draw initial and final position color
    initialSpot = windowGrid[initialPosition[0]][initialPosition[1]]
    initialSpot.ColorStartPosition()
    finalSpot = windowGrid[finalPosition[0]][finalPosition[1]]
    finalSpot.ColorFinalPosition()

    while isGameRunning:
        Draw(window, windowGrid)

        # Possible events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isGameRunning = False
                QuitGame()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    isGameRunning = False
                    QuitGame()
                # if event.key == pygame.K_SPACE or event.key == pygame.K_KP_ENTER or event.key == pygame.enter:
                    # start game

# ==================== #


def OnMenuButtonClick(window, algorithm, isMenuRunning):
    currentAlgorithm = algorithm
    isMenuRunning = False
    pygame.quit()
    window = pygame.display.set_mode((GAME_WIDTH, GAME_WIDTH))
    pygame.display.set_caption(GAME_TITLE + " - " + algorithm)
    MainMapScreen(window)

# ==================== #


def QuitGame():
    pygame.quit()
    sys.exit()

# ==================== #


def MainMenu():

    click = False
    isMenuRunning = True
    gameWindow = pygame.display.set_mode((int(GAME_WIDTH / 2), int(GAME_WIDTH / 2)))
    pygame.display.set_caption(GAME_TITLE)

    while isMenuRunning:

        # fill menu window and create buttons
        gameWindow.fill(LIGHT_BLACK)
        button_1 = pygame.Rect(100, 100, 200, 50)
        button_2 = pygame.Rect(100, 200, 200, 50)

        # binding click events
        x, y = pygame.mouse.get_pos()
        if button_1.collidepoint((x, y)):
            if click:
                OnMenuButtonClick(gameWindow, A_ALGORITHM, isMenuRunning)
        if button_2.collidepoint((x, y)):
            if click:
                OnMenuButtonClick(gameWindow, BLIND_SEARCH_ALGORITHM, isMenuRunning)

        pygame.font.init()
        myfont = pygame.font.SysFont('Helvetica Neue', 30)
        nameFont = pygame.font.SysFont('Helvetica Neue', 15)

        # Mouse hover colors
        if button_1.collidepoint((x, y)) and not click:
            pygame.draw.rect(gameWindow, LIGHT_ORANGE, button_1)
        else:
            pygame.draw.rect(gameWindow, ORANGE, button_1)

        if button_2.collidepoint((x, y)) and not click:
            pygame.draw.rect(gameWindow, LIGHT_ORANGE, button_2)
        else:
            pygame.draw.rect(gameWindow, ORANGE, button_2)

        # render button text
        aStarText = myfont.render('A* Algorithm', True, (0, 0, 0))
        bSearchText = myfont.render('Blind Search', True, (0, 0, 0))
        gameWindow.blit(aStarText, (140, 115))
        gameWindow.blit(bSearchText, (140, 215))
        names = nameFont.render('Cesar Marrote Manzano & Victor Felipe dos Santos', True, (250,250,250))
        gameWindow.blit(names, (0,0))
        pygame.display.update()

        # Possible events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isMenuRunning = False
                QuitGame()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    isMenuRunning = False
                    QuitGame()
                    
            if event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    click = True

# ==================== #


MainMenu()
