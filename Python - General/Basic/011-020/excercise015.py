"""
Write a Python program to get the volume of a sphere with radius 6.

NOTE: My solution will be for user given radius.
"""

"""
SOLUTION:
"""

import math
import sys
from pathlib import Path

abspath = Path(__file__)
toolspath = abspath.parents[3]
sys.path.append(str(toolspath / 'tools'))

from GetFromUser import GetNonNegativeFloat

piVal = math.pi

print("Let's set the radius:")
radius = GetNonNegativeFloat()

print((4/3)*piVal*(radius**3))