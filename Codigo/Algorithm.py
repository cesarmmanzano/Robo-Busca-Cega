import pygame
import threading
from queue import PriorityQueue
from pygame.locals import *

import Commons
import Position
import GameWindow

def CalculatePathBasedOnCurrentAlgorithm (tree, start, end, window):
    isCurrentAlgorithmAStar = Commons.currentAlgorithm == Commons.A_ALGORITHM
    queue = PriorityQueue()
    path = [start]
    exploredPositions = set([])
    queue.put((0, start, path))
    exploredPositions.add(start)
    pathWeight = start.weight.__neg__()
    while queue:
        
        weight, position, currentPath = queue.get()
        position.ColorPosition(Commons.ORANGE)
        
        if position == end:
            for pos in currentPath:
                pos.ColorPosition(Commons.PATH_COLOR)
                pathWeight += pos.weight     
            visitedNodes = exploredPositions.__len__() - queue._qsize()       
            RenderTexts(window, visitedNodes.__str__(), pathWeight.__str__())  
            GameWindow.DrawWindow(window, tree)
            return
        
        for i in range(position.neighbors.__len__()):
            if position.neighbors[i] not in exploredPositions:
                if isCurrentAlgorithmAStar:
                    cost = weight + CalculateManhattanDistance(position.neighbors[i], end)
                else:
                    cost = weight + position.neighbors[i].weight
                queue.put((cost, position.neighbors[i], currentPath + [position.neighbors[i]]))
                exploredPositions.add(position.neighbors[i])
                position.neighbors[i].ColorPosition(Commons.BLACK)
        
        thread = threading.Thread(target=GameWindow.DrawWindow, args=[window, tree, False])
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

def RenderTexts(window, visitedNodes, pathWeight):
    window = pygame.display.set_mode((Commons.GAME_WIDTH, Commons.GAME_WIDTH + 30)) 
    window.fill(Commons.BACKGROUND_MENU_COLOR)           
    pygame.font.init()
    myfont = pygame.font.SysFont(Commons.HELVETICA_NEUE_FONT, 15)
    visitedPositions = myfont.render(Commons.VISITED_NODES + visitedNodes, True, Commons.WHITE)
    pathCost = myfont.render(Commons.PATH_TOTAL_WEIGHT + pathWeight, True, Commons.WHITE)    
    window.blit(visitedPositions, (5, Commons.GAME_WIDTH + 10))
    window.blit(pathCost, (130, Commons.GAME_WIDTH + 10))
    pygame.display.update()