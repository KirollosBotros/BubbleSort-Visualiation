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
SIDE_MARGIN = 5
BOTTOM_MARGIN = 5
LEN = 70
DELAY = 1
first = False

#Create window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

#initialize set of towers with random lengths
def reset():
	arr.clear()
	for i in range(LEN):
		arr.append(random.random()*11)
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

#main loop
def main():
	run = True
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				sort()
			if event.type == pygame.KEYDOWN:
				reset()
				sort()

		def drawAll(array):
			counter = 0
			for i in range(len(array)):
				TOWER_X = SIDE_MARGIN+counter*((WIDTH-SIDE_MARGIN*2)/(len(array)))
				TOWER_Y = HEIGHT - BOTTOM_MARGIN - array[i]*40
				TOWER_W = ((WIDTH-SIDE_MARGIN*2)/(len(array)))*(7/9)
				TOWER_H = array[i]*40
				TOWER_COL = (0, array[i]*40/2, 0)
				towers.append(tower(TOWER_X, TOWER_Y, TOWER_W, TOWER_H , TOWER_COL))
				towers[i].drawTower(WIN)
				counter += 1
		
		WIN.fill((225, 250, 200))
		drawAll(arr)
		pygame.display.update()

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
			print("Done")
			first = True
main()