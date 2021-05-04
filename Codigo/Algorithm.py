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
        if position != start and isCurrentAlgorithmAStar:
            weight -= CalculateManhattanDistance(position, end)
            
        if position == end:
            for pos in currentPath:
                pos.ColorPosition(Commons.YELLOW)
                pathWeight += pos.weight
            visitedNodes = (exploredPositions.__len__() - queue._qsize()).__str__()
            RenderTexts(window, visitedNodes, pathWeight.__str__())
            GameWindow.DrawWindow(window, tree)
            return
        
        for i in range(position.neighbors.__len__()):
            if isCurrentAlgorithmAStar:
                cost = weight + position.neighbors[i].weight + CalculateManhattanDistance(position.neighbors[i], end)
            else:
                cost = weight + position.neighbors[i].weight
            if position.neighbors[i] not in exploredPositions:                
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
    return abs(end.row - position.row) + abs(end.column - position.column)

def RenderTexts(window, visitedNodes, pathWeight):
    window = pygame.display.set_mode((Commons.GAME_WIDTH, Commons.GAME_WIDTH + 30))
    window.fill(Commons.LIGHT_BLACK)
    Commons.RenderText(window, (Commons.VISITED_NODES + visitedNodes), (5, Commons.GAME_WIDTH + 10))
    Commons.RenderText(window, (Commons.PATH_TOTAL_WEIGHT + pathWeight), (130, Commons.GAME_WIDTH + 10))