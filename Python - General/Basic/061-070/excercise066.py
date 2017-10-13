"""
Write a Python program to calculate body mass index.
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

def calculateBMI(height, mass):
    height_meters = height/100
    return mass/(height_meters**2)

#get the height
print("Give me your height (in cm):")
height = GetNonNegativeInteger()

#get the mass
print("Give me your mass (in kg):")
mass = GetNonNegativeInteger()

print("BMI index: %f" % calculateBMI(height, mass))