import pygame
import sys
import math
from queue import PriorityQueue
from pygame.locals import *

import Commons
import Position

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

            spot = Position.Position(i, j, gap, color, weight)
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
                if event.key == pygame.K_SPACE or event.key == pygame.K_KP_ENTER:
                    for i in windowGrid:
                        for j in i:                            
                            j.CreateNeighbors(windowGrid)
