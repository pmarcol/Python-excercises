"""
Write a Python program which accepts the radius of a circle from the user and compute the area.
Sample Output : 
r = 1.1
Area = 3.8013271108436504
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

pivalue = math.pi

print("Let's set the radius:")
radius = GetNonNegativeFloat()

area = pivalue*(radius**2)
print(area)