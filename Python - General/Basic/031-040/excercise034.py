"""
Write a Python program to sum of two given integers.
However, if the sum is between 15 to 20 it will return 20
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

def specialSum(a, b):
    output = a + b
    if(15<= output <= 20): output = 20
    return output

while True:
    myList = GetListOfIntegers()
    if(len(myList) != 2):
        print("You should give exactly two numbers. Try again.")
        continue
    else:
        break

print(specialSum(myList[0],myList[1]))