"""
Write a python program to sum of the first n positive integers.
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

n = GetPositiveInteger()

def SumOfFirstIntegers(n):
    return (n*(n+1)//2)

print(SumOfFirstIntegers(n))
