import pygame
import Commons

class Position:
    def __init__(self, row, column, color, weight):
        self.row = row
        self.column = column
        self.color = color        
        self.weight = weight
        self.neighbors = []

    def ColorPosition(self, color):
        self.color = color
        
    def Draw(self, window):
        pygame.draw.rect(window, self.color, (self.column * Commons.SQUARE_SIZE, self.row * Commons.SQUARE_SIZE, Commons.SQUARE_SIZE, Commons.SQUARE_SIZE))    

    def CreateNeighbors(self, grid):
        self.neighbors = []

        # UP
        if self.row > 0:
            self.neighbors.append(grid[self.row - 1][self.column])

        # LEFT
        if self.column < Commons.GAME_ROWS - 1:
            self.neighbors.append(grid[self.row][self.column + 1])
            
        # DOWN
        if self.row < Commons.GAME_ROWS - 1:
            self.neighbors.append(grid[self.row + 1][self.column])
            
        # RIGHT
        if self.column > 0:
            self.neighbors.append(grid[self.row][self.column - 1])

    def __lt__(self, other):
        return True