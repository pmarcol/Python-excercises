"""
Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.
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

def specialSum(num1, num2, num3):
    result = num1 + num2 + num3
    if(num1==num2 or num2==num3 or num1==num3):
        result = 0
    return result

while True:
    myList = GetListOfIntegers()
    if(len(myList) != 3):
        print("You should give exactly three numbers. Try again.")
        continue
    else:
        break

print(specialSum(myList[0],myList[1],myList[2]))