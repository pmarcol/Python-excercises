"""
Write a Python program to compute the future value of a specified principal amount,
rate of interest, and a number of years.
Test Data : amt = 10000, int = 3.5, years = 7
Expected Output : 12722.79
"""

"""
SOLUTION:
"""

import sys
from pathlib import Path

abspath = Path(__file__)
toolspath = abspath.parents[3]
sys.path.append(str(toolspath / 'tools'))

from GetFromUser import GetNonNegativeFloat, GetNonNegativeInteger

def calculateFutureValue(origAmount, intRate, numberOfYears):
    factor = 1 + (intRate/100)
    return origAmount * ((factor)**numberOfYears)

amt = GetNonNegativeFloat()
rate = GetNonNegativeFloat()
yrs = GetNonNegativeInteger()

print(calculateFutureValue(amt, rate, yrs))