"""
Write a Python program to convert the distance (in feet) to inches, yards, and miles.
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

feetConversionRatioTable = {
    "inches" : 12,
    "yards" : 1/3,
    "miles" : 1/5280
}

def feetConverter(feet, targetUnit):
    try:
        ratio = feetConversionRatioTable[targetUnit]
    except KeyError:
        print("Unknown target unit.")
        return
    else:
        return feet*ratio


#Get the feet:
print("Let's set the distance (in feet):")
feet = GetNonNegativeInteger()

print("%d feet is %s inches." % (feet, feetConverter(feet,"inches")))
print("%d feet is %s yards." % (feet, feetConverter(feet,"yards")))
print("%d feet is %s miles." % (feet, feetConverter(feet,"miles")))