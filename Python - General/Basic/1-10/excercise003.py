"""
Write a Python program to display the current date and time.
Sample Output : 
Current date and time : 
2014-07-05 14:34:14
"""

"""
SOLUTION:
"""

import datetime
dateNow = datetime.datetime.now()
dateString = "%d-%02d-%02d %02d:%02d:%02d" % (dateNow.year,
dateNow.month,
dateNow.day,
dateNow.hour,
dateNow.minute,
dateNow.second)

print(dateString)