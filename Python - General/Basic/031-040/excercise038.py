"""
Write a Python program to solve (x + y) * (x + y).
Test Data : x = 4, y = 3
Expected Output : (4 + 3) ^ 2) = 49
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

def myFunction(a, b):
    return (a+b)**2

while True:
    myList = GetListOfIntegers()
    if(len(myList) != 2):
        print("You should give exactly two numbers. Try again.")
        continue
    else:
        break

print(myFunction(myList[0],myList[1]))