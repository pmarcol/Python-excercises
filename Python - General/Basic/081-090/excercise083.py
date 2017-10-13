"""
Write a Python program to test if a certain number is greater than all numbers of a list.
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

from GetFromUser import GetListOfIntegers, GetInteger

def isGreater(myNum, myList):
    if(myNum > max(myList)): return True
    else: return False

myNum = GetInteger()
while True:
    myList = GetListOfIntegers()
    if(len(myList)<1):
        print("You should give at least one value.")
        continue
    else:
        break

print(isGreater(myNum, myList))