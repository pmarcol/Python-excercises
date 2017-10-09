"""
Write a Python program to count the number 4 in a given list.
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

from GetFromUser import GetListOfIntegers

def countFours(myList):
    return myList.count(4)

myList = GetListOfIntegers

print("Given list contains %d 4's." % (countFours(myList)))