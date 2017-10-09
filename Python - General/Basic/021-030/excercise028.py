"""
Write a Python program to print all even numbers from a given numbers list in the same order
and stop the printing if any numbers that come after 237 in the sequence.

numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]

NOTE: There is probably a bug in solution. (x == 248)?!
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

def makeListOfEvenNumbersAndStopAt237(myList):
    outputList = []
    for n in myList:
        if(n==237):
            break
        elif(n%2==0):
            outputList.append(n)
    return outputList

myList = GetListOfIntegers()

print("Output list: %s" % makeListOfEvenNumbersAndStopAt237(myList))