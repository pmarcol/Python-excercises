"""
Write a Python program to perform an action if a condition is true.
Given a variable name, if the value is 1, display the string
"First day of a Month!"
and do nothing if the value is not equal.
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

from GetFromUser import GetInteger

def mySpecialFunc(val):
    if (val == 1):
        print("First day of a Month!")

myNum = GetInteger()

mySpecialFunc(myNum)
