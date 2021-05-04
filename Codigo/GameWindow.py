import pygame
from pygame.locals import *

import Commons
import Position
import Algorithm

def MainMapScreen(window):

    file = ReadFile()
    initialPosition = file[0]  # initialPosition[i, j]
    finalPosition = file[1]  # finalPosition[i, j]

    windowGrid = BuildInitialWindow(file[2])

    # draw initial and final position color
    initialSpot = windowGrid[initialPosition[0]][initialPosition[1]]
    initialSpot.ColorPosition(Commons.GREEN)
    finalSpot = windowGrid[finalPosition[0]][finalPosition[1]]
    finalSpot.ColorPosition(Commons.RED)

    while True:

        DrawWindow(window, windowGrid)

        # Possible events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Commons.QuitGame()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    Commons.QuitGame()

                if event.key == pygame.K_SPACE or event.key == pygame.K_KP_ENTER:
                    for i in windowGrid:
                        for j in i:
                            j.CreateNeighbors(windowGrid)
                    Algorithm.CalculatePathBasedOnCurrentAlgorithm(windowGrid, initialSpot, finalSpot, window)

                if event.key == pygame.K_r:
                    window = pygame.display.set_mode((Commons.GAME_WIDTH, Commons.GAME_WIDTH))
                    windowGrid = BuildInitialWindow(file[2])
                    initialSpot = windowGrid[initialPosition[0]][initialPosition[1]]
                    initialSpot.ColorPosition(Commons.GREEN)
                    finalSpot = windowGrid[finalPosition[0]][finalPosition[1]]
                    finalSpot.ColorPosition(Commons.RED)
                    pygame.display.update()
                                 
# ==================== #

def ReadFile():

    with open(Commons.FILE_NAME, 'r') as f:
        startI, startJ = [int(x) for x in next(f).split(',')]
        endI, endJ = [int(x) for x in next(f).split(',')]
        startPosition = [startI, startJ]
        finalPosition = [endI, endJ]
        gameMap = [[int(num) for num in line.split(',')] for line in f]

    # result [ [start], [final], [map] ]
    result = []
    result.append(startPosition)
    result.append(finalPosition)
    result.append(gameMap)

    return result

# ==================== #

def BuildInitialWindow(grid):
    windowGrid = []
    for i in range(Commons.GAME_ROWS):
        windowGrid.append([])
        for j in range(Commons.GAME_ROWS):

            if grid[i][j] == 1:
                color = Commons.LIGHT_GREEN
                weight = 1
            elif grid[i][j] == 2:
                color = Commons.LIGHT_BROWN
                weight = 5
            elif grid[i][j] == 3:
                color = Commons.LIGHT_BLUE
                weight = 10
            elif grid[i][j] == 4:
                color = Commons.LIGHT_RED
                weight = 15

            position = Position.Position(i, j, color, weight)
            windowGrid[i].append(position)

    return windowGrid

# ==================== #                        

def DrawWindow(window, grid, shouldDrawLine = True):

    for i in grid:
        for position in i:
            position.Draw(window)

    if shouldDrawLine:
        for i in range(Commons.GAME_ROWS):
            posy = i * Commons.SQUARE_SIZE
            pygame.draw.line(window, Commons.BLACK, (0, posy), (Commons.GAME_WIDTH, posy))
            for j in range(Commons.GAME_ROWS):
                posx = j * Commons.SQUARE_SIZE
                pygame.draw.line(window, Commons.BLACK, (posx, 0), (posx, Commons.GAME_WIDTH))

    pygame.display.update()