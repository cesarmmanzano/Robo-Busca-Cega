import pygame
import sys
import math
from queue import PriorityQueue
from pygame.locals import *
import Commons

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
        self.total_rows = Commons.GAME_ROWS
        self.weight = weight

    def GetWeight(self):
        return self.weight

    def IsStartPosition(self):
        return self.color == Commons.WHITE

    def IsEndPosition(self):
        return self.color == Commons.BLACK

    def ColorStartPosition(self):
        self.color = Commons.WHITE

    def ColorFinalPosition(self):
        self.color = Commons.BLACK

    def Draw(self, window):
        pygame.draw.rect(window, self.color,
                         (self.x, self.y, self.width, self.width))

    # the methods below are not used yet. Some of them will not be necessary
    def GetCurrentPosition(self):
        return self.row, self.col

    def IsClosed(self):
        return self.color == Commons.RED

    def IsOpen(self):
        return self.color == Commons.GREEN

    def Reset(self):
        self.color = Commons.WHITE

    def MakeClosed(self):
        self.color = Commons.RED

    def MakeOpen(self):
        self.color = Commons.GREEN

    def MakePath(self):
        self.color = Commons.PURPLE

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

    with open(Commons.FILE_NAME, 'r') as f:
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
    gap = Commons.GAME_WIDTH // Commons.GAME_ROWS
    for i in range(Commons.GAME_ROWS):
        pygame.draw.line(window, Commons.BLACK, (0, i * gap),
                         (Commons.GAME_WIDTH, i * gap))
        for j in range(Commons.GAME_ROWS):
            pygame.draw.line(window, Commons.BLACK, (j * gap, 0),
                             (j * gap, Commons.GAME_WIDTH))

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
    gap = Commons.GAME_WIDTH // Commons.GAME_ROWS
    for i in range(Commons.GAME_ROWS):
        windowGrid.append([])
        for j in range(Commons.GAME_ROWS):

            if grid[i][j] == 1:
                color = Commons.GREEN
                weight = 1
            elif grid[i][j] == 2:
                color = Commons.BROWN
                weight = 5
            elif grid[i][j] == 3:
                color = Commons.BLUE
                weight = 10
            elif grid[i][j] == 4:
                color = Commons.RED
                weight = 15

            spot = Spot(i, j, gap, color, weight)
            windowGrid[i].append(spot)

    return windowGrid

# ==================== #


def MainMapScreen(window):

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
                Commons.QuitGame()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    isGameRunning = False
                    Commons.QuitGame()
                # if event.key == pygame.K_SPACE or event.key == pygame.K_KP_ENTER or event.key == pygame.enter:
                    # start game
