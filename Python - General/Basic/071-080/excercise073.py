"""
Write a Python program to calculate midpoints of a line.
"""

"""
SOLUTION:
"""

import sys
from pathlib import Path
from math import sqrt

abspath = Path(__file__)
toolspath = abspath.parents[3]
sys.path.append(str(toolspath / 'tools'))

from GetFromUser import GetListOfFloats

def calculateMiddle(point1, point2):
    return [(point1[0] + point2[0])/2, (point1[1] + point2[1])/2]

print("Let's set coordinates for first point:")
while True:
    coordinates1 = GetListOfFloats()
    if(len(coordinates1) != 2):
        print('You should give exactly two coordinates.')
        continue
    else:
        break

print("Let's set coordinates for second point:")
while True:
    coordinates2 = GetListOfFloats()
    if(len(coordinates2) != 2):
        print('You should give exactly two coordinates.')
        continue
    else:
        break

print(calculateMiddle(coordinates1, coordinates2))