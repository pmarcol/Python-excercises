"""
 Write a Python program that will return true if the two given integer values are equal
 or their sum or difference is 5. 
"""

"""
SOLUTION:
"""

import sys
from pathlib import Path

abspath = Path(__file__)
toolspath = abspath.parents[3]
sys.path.append(str(toolspath / 'tools'))

from GetFromUser import GetListOfIntegers

def myIndicator(a, b):
    return ((a==b) or (abs(a-b) == 5) or (a+b == 5))

while True:
    myList = GetListOfIntegers()
    if(len(myList) != 2):
        print("You should give exactly two numbers. Try again.")
        continue
    else:
        break

print(myIndicator(myList[0],myList[1]))