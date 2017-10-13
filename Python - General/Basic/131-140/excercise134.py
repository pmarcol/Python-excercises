"""
Write a Python program to input two integers in a single line.

NOTE: Maybe my solution is not the most trivial, but I will make use of previously prepared code for getting an user input.
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

while True:
    myList = GetListOfIntegers()
    if(len(myList) != 2):
        print("You should give exactly two numbers. Try again.")
        continue
    else:
        break

print("Your numbers are: %d and %d" % (myList[0], myList[1]))