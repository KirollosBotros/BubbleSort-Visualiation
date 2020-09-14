import pygame

#Tower class that describes a single tower object to be sorted be heights
class tower():
	def __init__(self, x, y, width, height, colour):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.colour = colour
	
	def drawTower(self, win):
		pygame.draw.rect(win, self.colour, (self.x, self.y, self.width, self.height))