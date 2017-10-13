"""
Write a Python program to test whether a number is within 100 of 1000 or 2000.
"""

"""
SOLUTION:
"""

import sys
from pathlib import Path

abspath = Path(__file__)
toolspath = abspath.parents[3]
sys.path.append(str(toolspath / 'tools'))

from GetFromUser import GetInteger

def closeTo1000or2000(num):
    return(min(abs(1000-num), abs(2000-num))<=100)

myInt = GetInteger()

print('%d is within 100 of 1000 or 2000: %s' % (myInt, closeTo1000or2000(myInt)))