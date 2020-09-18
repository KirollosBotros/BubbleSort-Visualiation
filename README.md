# BubbleSort-Visualiation
A graphic visualization of the Bubble Sort sorting algorithm created in python using the 2D graphics module pygame

## The Program:
* When the program is intially run, an array of tower objects are generated with random heights. Their shade of green is associated with their heights with the shorter towers having a higher green value in their RGB (appears brighter) and taller towers having a lower green value in their RGB (appears darker).

![GitHub Logo](/images/start.JPG)

* When the user clicks anywhere on the window, the array of towers is sorted using the bubble sort algorithm. Between each iteration of the sort, there is a small delay (customizable) to allow the user to visually see the array get sorted. Once the array of towers is fully sorted, the towers will appear in increasing order (from left to right) with their shades of green going from light to dark. The user can click anywhere on the window again to reset the array of towers randomly and start sorting.

![GitHub Logo](/images/end.JPG)

* This visualization has been programed dynamically so that the number of towers, delay and colours can be customized easily by changing the constants. The following is a map of the constants:
	* "COL" (initialized at GREEN): the colour theme for the visualization
	* "LEN" (initialized at 50): the number of towers
	* "DELAY" (initialized at 2): the number of milliseconds to wait before each iteration in the sorting algorithm

## Examples of Different Looks: 

### Blue theme with 100 towers:

![GitHub Logo](/images/blue_start.JPG)
![GitHub Logo](/images/blue_end.JPG)

### Red theme with 25 towers:

![GitHub Logo](/images/red_start.JPG)
![GitHub Logo](/images/red_end.JPG)