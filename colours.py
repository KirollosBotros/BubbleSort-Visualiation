#Colour Constants
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
RED_BACK = (250,225,200)
GREEN_BACK = (225,250,200)
BLUE_BACK = (200,225,250)

#fuction to get the background colour based on the chosen colour theme
def getBack(COL):
	if COL == RED:
		return RED_BACK
	elif COL == GREEN:
		return GREEN_BACK
	else:
		return BLUE_BACK

#function to calculate the specific shade of the colour theme for each tower based on their heights
def getTowerCol(col, array, i):
		if col == RED:
			return (255-array[i]*18.88,0,0)
		elif col == GREEN:
			return (0,255-array[i]*18.88,0)
		else:
			return (0,0,255-array[i]*18.88)