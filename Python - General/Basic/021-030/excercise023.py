"""
Write a Python program to get the n (non-negative integer) copies of the
first 2 characters of a given string.
Return the n copies of the whole string if the length is less than 2.
"""

"""
SOLUTION:
"""

import sys
from pathlib import Path

abspath = Path(__file__)
toolspath = abspath.parents[3]
sys.path.append(str(toolspath / 'tools'))

from GetFromUser import GetNonNegativeInteger

def multiplyStringNTimes(myStr, myInt):
    return myInt * myStr

myInt = GetNonNegativeInteger()

myString = input('Give a string:')

print(multiplyStringNTimes(myString[:2],myInt))
