"""
Write a Python program to sort three integers without using conditional statements and loops. 
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

def specialSort(num1, num2, num3):
    out1 = min(num1, num2, num3)
    out3 = max(num1, num2, num3)
    out2 = num1 + num2 + num3 - out1 - out3
    return out1, out2, out3

while True:
    myList = GetListOfIntegers()
    if(len(myList) != 3):
        print("You should give exactly 3 numbers. Try again.")
        continue
    else:
        break

print("Sorted: %d, %d, %d" % specialSort(myList[0], myList[1], myList[2]))