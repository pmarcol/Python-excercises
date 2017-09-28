"""
Write a Python program to compute the greatest common divisor (GCD) of two positive integers.
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

from GetFromUser import GetPositiveInteger

#Euclidean Algorithm:
def getGCD(a,b):
    x = max(a, b)
    y = min(a, b)
    if(x%y == 0): return y
    temp = 0
    rem = y
    nextrem = x - (x//y)*y
    while(nextrem > 0):
        temp = rem
        rem = nextrem
        nextrem = temp - (temp//nextrem)*nextrem
    
    return rem

print("Let's set the first number:")
myInt1 = GetPositiveInteger()

print("Let's set the second number:")
myInt2 = GetPositiveInteger()

print("GCD of %d and %d is %d." % (myInt1,myInt2,getGCD(myInt1,myInt2)))