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
    initialSpot.ColorPosition(Commons.START_POSITION_COLOR)
    finalSpot = windowGrid[finalPosition[0]][finalPosition[1]]
    finalSpot.ColorPosition(Commons.FINAL_POSITION_COLOR)

    while isGameRunning:
        hasGameStarted = False
        Draw(window, windowGrid)

        # Possible events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isGameRunning = False
                Commons.QuitGame()
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    isGameRunning = False
                    Commons.QuitGame()
                    
                if event.key == pygame.K_SPACE or event.key == pygame.K_KP_ENTER and not hasGameStarted:
                    hasGameStarted = True
                    for i in windowGrid:
                        for j in i:
                            j.CreateNeighbors(windowGrid)                                            
                    CalculatePathBasedOnCurrentAlgorithm(windowGrid, initialSpot, finalSpot, window)
                    # if Commons.currentAlgorithm == Commons.A_ALGORITHM:
                    #     AStartAlgorithm(windowGrid, initialSpot, finalSpot, window)
                    # else:
                    #     BlindSearchAlgorithm(windowGrid, initialSpot, finalSpot, window)
                        
                if event.key == pygame.K_r:  
                    windowGrid = BuildInitialWindow(file[2])
                    initialSpot = windowGrid[initialPosition[0]][initialPosition[1]]
                    initialSpot.ColorPosition(Commons.START_POSITION_COLOR)
                    finalSpot = windowGrid[finalPosition[0]][finalPosition[1]]
                    finalSpot.ColorPosition(Commons.FINAL_POSITION_COLOR)     
                                 
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
                        
    
def Draw(window, grid, shouldDrawLine = True):

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
            
# ==================== #

def CalculatePathBasedOnCurrentAlgorithm (tree, start, end, window):
    queue = PriorityQueue()
    path = [start]
    exploredPositions = set([])
    queue.put((0, start, path))
    exploredPositions.add(start)
    w = 0
    while queue:            
                    
        weight, position, currentPath = queue.get()
        position.ColorPosition(Commons.ORANGE)
        
        if position == end:
            currentPath += [end]
            for i in currentPath:
                i.ColorPosition(Commons.YELLOW) 
                w += i.weight               
            print(weight)
            print(w)
            Draw(window, tree)
            return
        
        for i in range(position.neighbors.__len__()):
            if position.neighbors[i] not in exploredPositions:
                if Commons.currentAlgorithm == Commons.A_ALGORITHM:
                    cost = weight + CalculateManhattanDistance(position.neighbors[i], end)
                else:
                    cost = weight + position.neighbors[i].weight        
                queue.put((cost, position.neighbors[i], currentPath + [position.neighbors[i]]))                
                exploredPositions.add(position.neighbors[i])
                position.neighbors[i].ColorPosition(Commons.BLACK)
        
        thread = threading.Thread(target=Draw, args=[window, tree, False])
        thread.start()
        thread.join()
    
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Commons.QuitGame()
                    
            if event.type == pygame.QUIT:
                Commons.QuitGame()

def CalculateManhattanDistance(position, end):
    return abs(position.row - end.row) + abs(position.column - end.column)        