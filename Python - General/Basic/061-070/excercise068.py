"""
Write a Python program to calculate the sum of the digits in an integer.
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

def sumOfDigits(num):
    num_str = str(num)
    result = 0
    for digit in num_str:
        result += int(digit)
    return result

myNum = GetNonNegativeInteger()

print("Sum of digits in %d is %d." % (myNum, sumOfDigits(myNum)))