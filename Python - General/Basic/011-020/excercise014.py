"""
Write a Python program to calculate number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days 
"""

"""
SOLUTION:
"""

from datetime import date

firstDate = date(2014, 7, 2)
secondDate = date(2014, 7, 11)

print(str(abs((secondDate - firstDate).days)) + ' day(s)')