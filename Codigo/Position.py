import pygame
from pygame.locals import *
import Commons

class Position:
    def __init__(self, row, col, color, weight):
        self.row = row
        self.col = col
        self.color = color
        self.neighbors = []
        self.weight = weight

    def ColorStartPosition(self):
        self.color = Commons.START_POSITION_COLOR

    def ColorFinalPosition(self):
        self.color = Commons.FINAL_POSITION_COLOR

    def Draw(self, window):
        pygame.draw.rect(window, self.color, (self.col * Commons.SQUARE_SIZE, self.row * Commons.SQUARE_SIZE, Commons.SQUARE_SIZE, Commons.SQUARE_SIZE))

    def MakePath(self):
        self.color = Commons.YELLOW

    def CreateNeighbors(self, grid):
        self.neighbors = []

        # UP
        if self.row > 0:
            position = grid[self.row - 1][self.col]
            self.neighbors.append(position)

        # LEFT
        if self.col < Commons.GAME_ROWS - 1:
            position = grid[self.row][self.col + 1]
            self.neighbors.append(position)
            
        # DOWN
        if self.row < Commons.GAME_ROWS - 1:
            position = grid[self.row + 1][self.col]
            self.neighbors.append(position)
            
        # RIGHT
        if self.col > 0:
            position = grid[self.row][self.col - 1]
            self.neighbors.append(position)

    def __lt__(self, other):
        return False