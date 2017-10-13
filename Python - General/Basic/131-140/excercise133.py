"""
Write a Python program to calculate the time runs (difference between start and current time) of a program.

NOTE: Similar exercise was already done before (excercise057), but this time I qill try to make it using a decorator.
"""

"""
SOLUTION:
"""

import time

def timing(f):
    def wrap(*args):
        timeStart = time.time()
        out = f(*args)
        timeStop = time.time()
        print("Execution of %s function took %0.3f s" % (f.__name__, (timeStop - timeStart)))
        return out
    return wrap

@timing
def SomeTimekillingFunc1():
    time.sleep(1.233)
    return

SomeTimekillingFunc1()