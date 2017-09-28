"""
 Write a Python program to create a histogram from a given list of integers.
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

def histogram(myList):
    output = ''
    for n in myList:
        times = n
        bar = ''
        while( times > 0 ):
            bar += '*'
            times = times - 1
        output += '\n'
        output += bar
    return output

while True:
    myList = GetListOfIntegers()
    if(min(myList) < 0):
        print("All integers should be nonegative. Try again.")
        continue
    else:
        break

print(histogram(myList))