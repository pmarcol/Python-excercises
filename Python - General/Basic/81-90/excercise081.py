"""
Write a Python program to concatenate N strings.
"""

"""
SOLUTION:
"""

import sys
import os
from pathlib import Path
from math import sqrt

abspath = Path(__file__)
toolspath = abspath.parents[3]
sys.path.append(str(toolspath / 'tools'))

from GetFromUser import GetPositiveInteger

def myConcat(myList):
    return ''.join(myList)

reps = GetPositiveInteger()
theList = []

for i in range(reps):
    theList.append(input("Give me the string number %d:" % (i+1)))

print(myConcat(theList))