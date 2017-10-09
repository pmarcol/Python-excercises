"""
Write a Python program to check whether a specified value is contained in a group of values.
Test Data : 
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False
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

from GetFromUser import GetInteger, GetListOfIntegers

def listContainsElement(myList, myElement):
    return (myList.count(myElement) > 0)

myList = GetListOfIntegers()
myInt = GetInteger()

print("The list: %s contains %d: %s" % (myList, myInt, listContainsElement(myList,myInt)))