"""
Write a Python program to convert height (in feet and inches) to centimeters.
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

from GetFromUser import GetNonNegativeInteger

def ConvertToCm(ft, inch):
    feetToCmRatio = 30.48
    inchesToCmRatio = 2.54
    return (feet*feetToCmRatio + inches*inchesToCmRatio)

#Get the feet:
print("Lets set the feet:")
feet = GetNonNegativeInteger()

#Get the inches:
print("Let's set the inches:")
inches = GetNonNegativeInteger()

print("%d ft and %d in is %f cm." % (feet, inches, ConvertToCm(feet, inches)))