import random
import sys
 
import pygame
from pygame.locals import *
import time
pygame.init()
 
fpsClock = pygame.time.Clock()
TILESIZE = 1
width, height = 400, 400
screen = pygame.display.set_mode((width * TILESIZE, height * TILESIZE))
pygame.display.set_caption('Game of Life')
#Constants
DEAD = 0
ALIVE = 1
grid = []
#Textures
textures = {
			DEAD: pygame.image.load("textures/dead2.png"),
			ALIVE: pygame.image.load("textures/alive1.png")
		}
for i in range(1, width):
	app = []
	for i in range(1, width):
		chance = random.randint(0, 100)
		if chance >= 10:
			square = DEAD
		else:
			square = ALIVE
		app.append(square)
	grid.append(app)

def main(cells):

	for i in range(0, len(cells)-1):
		for n in range(0, width - 1):
			liveN = 0
			try:
				if cells[i][n - 1] == ALIVE:
					liveN += 1
				if cells[i][n+1] == ALIVE:
					liveN += 1
				if cells[i-1][n] == ALIVE:
					liveN += 1
				if cells[i-1][n + 1] == ALIVE:
					liveN += 1
				if cells[i-1][n-1] == ALIVE:
					liveN += 1
				if cells[i + 1][n] == ALIVE:
					liveN += 1
				if cells[i + 1][n+1] == ALIVE:
					liveN += 1
				if cells[i + 1][n -1] == ALIVE:
					liveN += 1
			except:
				continue
			#Death by Isolation
			if liveN <= 1:
				cells[i][n] = DEAD
			#Death by Overcrowding
			if liveN >= 4:
				cells[i][n] = DEAD
			#Birth Rule
			if liveN == 3:
				cells[i][n] = ALIVE
	screen.fill((0, 0, 0))

	for event in pygame.event.get():
		if event.type == QUIT:
		  pygame.quit()
		  sys.exit()

	# Update.

	# Draw.
	for i in range(0, len(cells)):
		for n in range(0, width - 1):
			screen.blit(textures[cells[i][n]], (i * TILESIZE, n * TILESIZE))

	pygame.display.flip()
	time.sleep(0.1)


while True:
	main(grid) 