"""
Write a Python program to check if a number is positive, negative or zero.
"""

"""
SOLUTION:
"""

import sys
from pathlib import Path

abspath = Path(__file__)
toolspath = abspath.parents[3]
sys.path.append(str(toolspath / 'tools'))

from GetFromUser import GetFloat

def signum(number):
    if number < 0:
        return "Negative"
    elif number == 0:
        return "0"
    else:
        return "Positive"

myNum = GetFloat()

print(signum(myNum))