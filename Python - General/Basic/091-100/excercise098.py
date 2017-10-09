"""
Write a Python program to get the system time.
"""

"""
SOLUTION:
"""

def getSysTime1():
    import datetime
    return datetime.datetime.now().time()

def getSysTime2():
    import time
    return time.ctime()

print(getSysTime1())
print(getSysTime2())