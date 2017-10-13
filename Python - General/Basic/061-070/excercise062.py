"""
Write a Python program to get an absolute file path.
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

def convertToSeconds(value, originalUnit):
    try:
        ratio = toSecondsConvertionRatioTable[originalUnit]
    except KeyError:
        print("Unknown unit: %s" % originalUnit)
        return
    else:
        return value*ratio

toSecondsConvertionRatioTable = {
    "seconds" : 1,
    "minutes" : 60,
    "hours" : 60*60,
    "days" : 24*60*60
}

convertionValuesTable = {}

for myKey in toSecondsConvertionRatioTable.keys():
    print("%s:" % myKey)
    myValue = GetNonNegativeInteger()
    convertionValuesTable[myKey] = myValue

output = 0

for myKey in convertionValuesTable:
    output += convertToSeconds(convertionValuesTable[myKey], myKey)
    print("%d %s," % (myValue, myKey), end = " ")

print("give %d seconds in total" % output)
