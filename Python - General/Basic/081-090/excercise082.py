"""
Write a Python program to calculate the sum over a container.
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

from GetFromUser import GetListOfIntegers

myList = GetListOfIntegers() #This is the container (list). See the implementation of GetListOfIntegers for details

print(sum(myList))