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
SIDE_MARGIN = 10
BOTTOM_MARGIN = 5
LEN = 70
DELAY = 1

#Create window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

#initialize set of towers with random lengths
def reset():
	arr.clear()
	for i in range(LEN):
		arr.append(random.random()*11)

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
		reset()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
				sort()

		def drawAll(arr, col):
			counter = 0
			for i in range(len(arr)):
				towers.append(tower(SIDE_MARGIN+counter*((WIDTH-SIDE_MARGIN*2)/(len(arr))), HEIGHT - BOTTOM_MARGIN - arr[i]*40, ((WIDTH-SIDE_MARGIN*2)/(len(arr)))*(7/9), arr[i]*40, col))
				towers[i].drawTower(WIN)
				counter += 1
		
		drawAll(arr, RED)
		pygame.display.update()

		def sort():		
			while(notSorted(arr)):
				for i in range (len(arr)-1):
					WIN.fill((50))
					if arr[i] > arr[i+1]:
						swap(arr, i)
						towers.clear()
						drawAll(arr, GREEN)				
						pygame.time.wait(DELAY)
						pygame.display.update()	
			print("Done")
main()