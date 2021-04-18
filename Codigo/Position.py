import pygame
from pygame.locals import *
import Commons

class Position:
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
        self.neighborsWeight = []
    
    def GetNeighborWithLowestCost(self):
        cost = self.neighborsWeight[0]
        position = 0   
        for i in range(0, self.neighborsWeight.__len__()):
            if self.neighborsWeight[i] < cost: 
                cost = self.neighborsWeight[i]               
                position = i

        return self.neighbors[position]
        
    def IsStartPosition(self):
        return self.color == Commons.WHITE

    def IsEndPosition(self):
        return self.color == Commons.BLACK

    def ColorStartPosition(self):
        self.color = Commons.WHITE

    def ColorFinalPosition(self):
        self.color = Commons.BLACK

    def Draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.width))

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
        self.neighborsWeight = []            

        # UP
        if self.row > 0:
            position = grid[self.row - 1][self.col]
            self.neighbors.append(position)
            self.neighborsWeight.append(position.weight)

        # RIGHT
        if self.col < self.total_rows - 1:
            position = grid[self.row][self.col + 1]
            self.neighbors.append(position)
            self.neighborsWeight.append(position.weight)           
            
        # DOWN
        if self.row < self.total_rows - 1:
            position = grid[self.row + 1][self.col]
            self.neighbors.append(position)
            self.neighborsWeight.append(position.weight)         
            
        # LEFT
        if self.col > 0:
            position = grid[self.row][self.col - 1]
            self.neighbors.append(position)
            self.neighborsWeight.append(position.weight)                                 

    def __lt__(self, other):
        return False