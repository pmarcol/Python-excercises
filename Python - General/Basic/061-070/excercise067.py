"""
Write a Python program to convert pressure in kilopascals to pounds per square inch,
a millimeter of mercury (mmHg) and atmosphere pressure.
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

kPaConversionRatioTable = {
    "ppsi" : 0.145037738,
    "mmhg" : 7.50061683,
    "atm" : 0.00986923267
}

def kPaConverter(kPa, targetUnit):
    try:
        ratio = kPaConversionRatioTable[targetUnit]
    except KeyError:
        print("Unknown target unit.")
        return
    else:
        return kPa*ratio

#get the kPa value:
print("Give me the pressure in kPa (non-negative integer):")
kPa = GetNonNegativeInteger()

for key in kPaConversionRatioTable:
    print("%d kPa is %f %s." % (kPa, kPaConverter(kPa, key), key))