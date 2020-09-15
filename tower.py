import pygame

#Tower class that describes a single tower object to be sorted by heights
class tower():
	def __init__(self, x, y, width, height, colour):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.colour = colour
	
	#draws a single tower given initialization parameters
	def drawTower(self, win):
		pygame.draw.rect(win, self.colour, (self.x, self.y, self.width, self.height))

	#changes colour of a tower to a colour specified as a parameter
	def changeCol(self, win, col):
		pygame.draw.rect(win, col, (self.x, self.y, self.width, self.height))
