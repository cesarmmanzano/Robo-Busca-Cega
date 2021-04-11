import pygame
import math
from queue import PriorityQueue

GAME_WIDTH = 800
GAME_ROWS = 42
GAME_WINDOW = pygame.display.set_mode((GAME_WIDTH, GAME_WIDTH))
pygame.display.set_caption("Robo Busca Cega")

FILE_NAME = 'index.txt'

# RGB Colors
GREEN = (151,224,103) #1 - Straight/Flat/Solid
BROWN = (119,93,68) #2 - Mountain
BLUE = (84,194,234) #3 - Swamp
RED = (201,94,82) #4 - Fire

YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165 ,0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)


# ==================== #

class Spot:
	def __init__(self, col, row, width, total_rows, color, weight):
		self.row = row
		self.col = col
		self.x = row * width
		self.y = col * width
		self.color = color
		self.neighbors = []
		self.width = width
		self.total_rows = total_rows
		self.weight = weight

	def get_weight(self):
		return self.weight

	def get_pos(self):
		return self.row, self.col

	def is_closed(self):
		return self.color == RED

	def is_open(self):
		return self.color == GREEN

	def is_barrier(self):
		return self.color == BLACK

	def is_start(self):
		return self.color == ORANGE

	def is_end(self):
		return self.color == TURQUOISE

	def reset(self):
		self.color = WHITE

	def ColorStartPosition(self):
		self.color = WHITE

	def make_closed(self):
		self.color = RED

	def make_open(self):
		self.color = GREEN

	def make_barrier(self):
		self.color = BLACK

	def ColorFinalPosition(self):
		self.color = BLACK

	def make_path(self):
		self.color = PURPLE

	def draw(self, win):
		pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

	def update_neighbors(self, grid):
		self.neighbors = []
		if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier(): # DOWN
			self.neighbors.append(grid[self.row + 1][self.col])

		if self.row > 0 and not grid[self.row - 1][self.col].is_barrier(): # UP
			self.neighbors.append(grid[self.row - 1][self.col])

		if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier(): # RIGHT
			self.neighbors.append(grid[self.row][self.col + 1])

		if self.col > 0 and not grid[self.row][self.col - 1].is_barrier(): # LEFT
			self.neighbors.append(grid[self.row][self.col - 1])

	def __lt__(self, other):
		return False

# ==================== #

def ReadFile():

	with open(FILE_NAME, 'r') as f:
		ws, hs = [int(x) for x in next(f).split(',')]
		we, he = [int(x) for x in next(f).split(',')]
		start = [ws,hs]
		end = [we,he]
		l = [[int(num) for num in line.split(',')] for line in f]
		
	result = []
	result.append(start)
	result.append(end)
	result.append(l)

	return result

# ==================== #

def DrawGrid(win, rows, width):
	gap = width // rows
	for i in range(rows):
		pygame.draw.line(win, BLACK, (0, i * gap), (width, i * gap))
		for j in range(rows):
			pygame.draw.line(win, BLACK, (j * gap, 0), (j * gap, width))

# ==================== #

def Draw(win, grid, rows, width):
	win.fill(WHITE)

	for row in grid:
		for spot in row:
			spot.draw(win)

	DrawGrid(win, rows, width)
	pygame.display.update()

# ==================== #

def BuildInitialWindow(rows, width, grid):
	gridWindow = []
	gap = width // rows	
	for i in range(rows):
		gridWindow.append([])
		for j in range(rows):
					
			if grid[i][j] == 1:
				color = GREEN
				weight = 1									
			if grid[i][j] == 2:
				color = BROWN
				weight = 5								
			if grid[i][j] == 3:
				color = BLUE
				weight = 10							
			if grid[i][j] == 4:
				color = RED	
				weight = 15	
			
			spot = Spot(i, j, gap, rows, color, weight)
			gridWindow[i].append(spot)
		
	return gridWindow
			
# ==================== #

def main(window, width):

	file = ReadFile()
	initialPosition = file[0] # initialPosition[i, j]
	finalPosition = file[1] # finalPosition[i, j]
	grid = file[2]

	windowGrid = BuildInitialWindow(GAME_ROWS, width, grid)
	
	isGameRunning = True

	while isGameRunning:	
		Draw(window, windowGrid, GAME_ROWS, width)
		initialSpot = windowGrid[initialPosition[0]][initialPosition[1]]
		initialSpot.ColorStartPosition()
		finalSpot = windowGrid[finalPosition[0]][finalPosition[1]]
		finalSpot.ColorFinalPosition()				
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				isGameRunning = False

# ==================== #

main(GAME_WINDOW, GAME_WIDTH)