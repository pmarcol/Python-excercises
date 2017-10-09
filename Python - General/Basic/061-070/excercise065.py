"""
Write a Python program to convert seconds to day, hour, minutes and seconds.
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

def secondsToDaysHoursMinutesSeconds(scnds):
    seconds = scnds
    days = seconds//(24*60*60)
    seconds = seconds % (24*60*60)
    hours = seconds//(60*60)
    seconds = seconds % (60*60)
    minutes = seconds//60
    seconds = seconds % 60
    return days, hours, minutes, seconds
    
#get the number of seconds:
print("Let's set the number of seconds:")
seconds = GetNonNegativeInteger()

print("%d day(s), %d hour(s), %d minute(s) and %d second(s)" % secondsToDaysHoursMinutesSeconds(seconds))
