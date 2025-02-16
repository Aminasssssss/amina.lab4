#Write a Python program to calculate the area of a trapezoid.
# Height: 5
# Base, first value: 5
# Base, second value: 6
# Expected Output: 27.5

import math 
height = float (input( ))
base1 = float (input( ))
base2 = float (input( ))

area = math.fsum([base1, base2])* height / 2

print(area)