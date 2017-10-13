"""
Write a Python program that will accept the base and height of a triangle and compute the area
"""

"""
SOLUTION:
"""

import sys
from pathlib import Path

abspath = Path(__file__)
toolspath = abspath.parents[3]
sys.path.append(str(toolspath / 'tools'))

from GetFromUser import GetNonNegativeFloat

def calculateArea(base, height):
    return 0.5*base*height

print("Let's set the base:")
base = GetNonNegativeFloat()

print("Let's set the height:")
height = GetNonNegativeFloat()

print("Area of the triangle: %s" % calculateArea(base,height))