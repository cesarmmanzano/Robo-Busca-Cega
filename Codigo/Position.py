import pygame
from pygame.locals import *
import Commons

class Position:
    def __init__(self, row, col, width, color, weight):
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

    def ColorStartPosition(self):
        self.color = Commons.START_POSITION_COLOR

    def ColorFinalPosition(self):
        self.color = Commons.FINAL_POSITION_COLOR

    def Draw(self, window):
        pygame.draw.rect(window, self.color, (self.y, self.x, self.width, self.width))

    def MakePath(self):
        self.color = Commons.YELLOW

    def CreateNeighbors(self, grid):
        self.neighbors = []
        self.neighborsWeight = []            

        # UP
        if self.row > 0:
            position = grid[self.row - 1][self.col]
            self.neighbors.append(position)
            self.neighborsWeight.append(position.weight)

        # LEFT
        if self.col < self.total_rows - 1:
            position = grid[self.row][self.col + 1]
            self.neighbors.append(position)
            self.neighborsWeight.append(position.weight)           
            
        # DOWN
        if self.row < self.total_rows - 1:
            position = grid[self.row + 1][self.col]
            self.neighbors.append(position)
            self.neighborsWeight.append(position.weight)         
            
        # RIGHT
        if self.col > 0:
            position = grid[self.row][self.col - 1]
            self.neighbors.append(position)
            self.neighborsWeight.append(position.weight)                                 

    def __lt__(self, other):
        return False