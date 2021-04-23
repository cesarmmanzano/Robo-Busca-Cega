import pygame
import threading
from queue import PriorityQueue
from pygame.locals import *

import Commons
import Position
import GameWindow

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
            for i in currentPath:
                i.ColorPosition(Commons.PATH_COLOR)
                w += i.weight
            print("Custo total (busca cega): ", weight)
            print("Peso total (a*): ", w - start.weight)
            GameWindow.DrawWindow(window, tree)
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