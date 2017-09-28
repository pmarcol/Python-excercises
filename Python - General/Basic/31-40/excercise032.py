"""
Write a Python program to get the least common multiple (LCM) of two positive integers.
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

# LCM calculation:
def getLCM(a,b):
    return (a*b)/getGCD(a,b)

print("Let's set the first number:")
myInt1 = GetPositiveInteger()

print("Let's set the second number:")
myInt2 = GetPositiveInteger()

print("LCM of %d and %d is %d." % (myInt1,myInt2,getLCM(myInt1,myInt2)))