#Write a Python program to calculate the area of a parallelogram.
# Length of base: 5
# Height of parallelogram: 6
# Expected Output: 30.0

import math
base = float(input())
height = float(input())

area = math.prod([base, height])
print(area)