"""
Write a Python program to print the calendar of a given month and year.
Note : Use 'calendar' module.
"""

"""
SOLUTION:
"""

import calendar

#get number of month
while True:
    try:
        theMonth = int(input('Give me number of the month:'))
        if (not(0<theMonth<13)):
            print('Incorrect number of month. Try again.')
            continue
    except ValueError:
        print('Incorrect input. Try again.')
        continue
    else:
        break

#get number of year
while True:
    try:
        theYear = int(input('Give me number of the year:'))
        if (not(0<theYear)):
            print('Incorrect number of year. Try again.')
            continue
    except ValueError:
        print('Incorrect input. Try again.')
        continue
    else:
        break

print(calendar.month(theYear,theMonth,1,1))