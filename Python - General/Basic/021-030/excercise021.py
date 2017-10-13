"""
Write a Python program to find whether a given number
(accept from the user) is even or odd, print out an appropriate message to the user.
"""

"""
SOLUTION:
"""

import sys
from pathlib import Path

abspath = Path(__file__)
toolspath = abspath.parents[3]
sys.path.append(str(toolspath / 'tools'))

from GetFromUser import GetInteger

def OddOrEven(num):
    if(num%2 == 0): return "even"
    else: return "odd"

myInt = GetInteger()

print("Given number (%d) is %s" %(myInt, OddOrEven(myInt)))