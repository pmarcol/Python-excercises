"""
Write a Python program to get the difference between a given number and 17,
if the number is greater than 17 return double the absolute difference.
"""

"""
SOLUTION:
"""

import sys
import os
from pathlib import Path

abspath = Path(__file__)
toolspath = abspath.parents[3]
sys.path.append(str(toolspath / 'tools'))

from GetFromUser import GetInteger

def difference17(num):
    if(num>17):
        return 2*abs(17-num)
    else:
        return abs(17-num)

myInt = GetInteger()

print(difference17(myInt))