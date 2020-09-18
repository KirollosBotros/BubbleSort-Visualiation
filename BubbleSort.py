import pygame
import random
from tower import *

#Constants
WIDTH = 1000
HEIGHT = 550
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)
arr = []
towers = []
counter = 0
SIDE_MARGIN = 3
BOTTOM_MARGIN = 3
LEN = 50
DELAY = 2

pygame.init()

#Create window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

#initialize set of towers with random lengths
def reset():
	arr.clear()
	for i in range(LEN):
		arr.append(random.random()*12)
reset()

#swap function
def swap(arr, pos):
	temp = arr[pos]
	arr[pos] = arr[pos+1]
	arr[pos+1] = temp

#function to check if an array arr is sorted
def notSorted(arr):
	for i in range (len(arr)-1):
		if arr[i] > arr[i+1]:
			return True
	return False

#initialize font and text
font = pygame.font.SysFont("timesnewroman", 50)
text = "Click to Start Visualization"
size = font.size(text)

#main loop
def main():
	run = True
	notFirst = False

	while run:
		#display label at the top of the screen
		label = font.render(text, 1, (0,0,0))
		WIN.blit(label, (WIDTH/2 - font.size(text)[0]/2, 10))
		pygame.display.update()

		#Event handler to check is WIN is closed or if mouse is pressed
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				sort()
				if notFirst:
					reset()
					sort()
				notFirst = True
		
		#draws all the towers according to their respective heights and colours in arr
		def drawAll(array):
			counter = 0
			for i in range(len(array)):
				TOWER_X = SIDE_MARGIN+counter*((WIDTH-SIDE_MARGIN*2)/(len(array)))
				TOWER_Y = HEIGHT - BOTTOM_MARGIN - array[i]*40
				TOWER_W = ((WIDTH-SIDE_MARGIN*2)/(len(array)))*(.85)
				TOWER_H = array[i]*40
				TOWER_COL = (0, 255-array[i]*18.88, 0)
				towers.append(tower(TOWER_X, TOWER_Y, TOWER_W, TOWER_H , TOWER_COL))
				towers[i].drawTower(WIN)
				counter += 1
		
		#draw inital unsorted towers on screen
		WIN.fill((225, 250, 200))
		drawAll(arr)
		
		#main sorting function: Bubble Sort
		def sort():		
			while(notSorted(arr)):
				for i in range (len(arr)-1):
					WIN.fill((225,250,200))
					if arr[i] > arr[i+1]:
						swap(arr, i)
						towers.clear()
						drawAll(arr)				
						pygame.time.wait(DELAY)
						pygame.display.update()	
			text = "Done"
main()