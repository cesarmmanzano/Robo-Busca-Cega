import pygame
import sys
import math
import threading
from queue import PriorityQueue
from pygame.locals import *

import Commons
import Position

# ==================== #

def MainMapScreen(window):

    file = ReadFile()
    initialPosition = file[0]  # initialPosition[i, j]
    finalPosition = file[1]  # finalPosition[i, j]

    windowGrid = BuildInitialWindow(file[2])

    isGameRunning = True
    hasGameStarted = False
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
                if event.key == pygame.K_SPACE or event.key == pygame.K_KP_ENTER and not hasGameStarted:
                    hasGameStarted = True
                    for i in windowGrid:
                        for j in i:
                            j.CreateNeighbors(windowGrid)                                            
                    if Commons.currentAlgorithm == Commons.A_ALGORITHM:
                        AStartAlgorithm(windowGrid, initialSpot, finalSpot, window)
                    else:
                        BlindSearchAlgorithm(windowGrid, initialSpot, finalSpot, window)    
                        
                if event.key == pygame.K_r:  
                    windowGrid = BuildInitialWindow(file[2])
                    initialSpot = windowGrid[initialPosition[0]][initialPosition[1]]
                    initialSpot.ColorStartPosition()
                    finalSpot = windowGrid[finalPosition[0]][finalPosition[1]]
                    finalSpot.ColorFinalPosition()     
                                 
# ==================== #

def ReadFile():

    with open(Commons.FILE_NAME, 'r') as f:
        ws, hs = [int(x) for x in next(f).split(',')]
        we, he = [int(x) for x in next(f).split(',')]
        startPosition = [ws, hs]
        finalPosition = [we, he]
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

            position = Position.Position(i, j, color, weight)
            windowGrid[i].append(position)

    return windowGrid

# ==================== #                   
                        
    
def Draw(window, grid, shouldDrawGrid = True):

    for i in grid:
        for position in i:
            position.Draw(window)

    if shouldDrawGrid:
        DrawGrid(window)
        
    pygame.display.update()

# ==================== #

def DrawGrid(window):
    for i in range(Commons.GAME_ROWS):
        pygame.draw.line(window, Commons.BLACK, (0, i * Commons.SQUARE_SIZE), (Commons.GAME_WIDTH, i * Commons.SQUARE_SIZE))
        for j in range(Commons.GAME_ROWS):
            pygame.draw.line(window, Commons.BLACK, (j * Commons.SQUARE_SIZE, 0), (j * Commons.SQUARE_SIZE, Commons.GAME_WIDTH))
            
# ==================== #

def BlindSearchAlgorithm(tree, start, end, window):
    queue = PriorityQueue()
    path = []
    exploredPositions = set([])    
    queue.put((0, start, path))
    exploredPositions.add(start)
    
    while queue:
        
        weight, position, currentPath = queue.get()          
        position.ColorPosition()  
           
        if position == end:
            currentPath += [end]
            for i in currentPath:
                i.ColorPath()
            Draw(window, tree)           
            return
        
        for i in range(0, position.neighbors.__len__()):
            if position.neighbors[i] not in exploredPositions:                               
                queue.put((weight + position.neighbors[i].weight, position.neighbors[i], currentPath + [position]))
                exploredPositions.add(position.neighbors[i])
                position.neighbors[i].ColorBorder()
        
        thread = threading.Thread(target=Draw, args=[window, tree, False])
        thread.start()

# ==================== #

def AStartAlgorithm(tree, start, end, window):
    print(Commons.A_ALGORITHM)
    
# ==================== #

def CalculateManhattanDistance(tree, position, end):   
     print('manhattan distance')