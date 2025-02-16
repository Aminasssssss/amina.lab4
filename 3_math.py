#Write a Python program to calculate the area of regular polygon.
# Input number of sides: 4
# Input the length of a side: 25
# The area of the polygon is: 625

import math 

sides = int(input())
side_length = float(input())

area = (sides * (side_length **2)) / (4* math.tan(math.pi / sides))
print(round(area, 2))