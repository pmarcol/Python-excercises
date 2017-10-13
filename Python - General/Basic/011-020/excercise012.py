"""
Write a Python program to print the calendar of a given month and year.
Note : Use 'calendar' module.
"""

"""
SOLUTION:
"""

import calendar
import sys
from pathlib import Path

abspath = Path(__file__)
toolspath = abspath.parents[3]
sys.path.append(str(toolspath / 'tools'))

from GetFromUser import GetPositiveInteger

#get number of month
print("Let's set the month.")
while True:
    theMonth = GetPositiveInteger()
    if (not(0<theMonth<13)):
        print('Incorrect number of month. Try again.')
        continue
    else:
        break

#get number of year
print("Let's set the year.")
while True:
    theYear = GetPositiveInteger()
    if (not(0<theYear)):
        print('Incorrect number of year. Try again.')
        continue
    else:
        break

print(calendar.month(theYear,theMonth,1,1))