"""
Write a Python program to determine profiling of Python programs.
Note: A profile is a set of statistics that describes how often and for how long various parts of the program executed.
These statistics can be formatted into reports via the pstats module. 
"""

"""
SOLUTION:
"""

import cProfile
import time

def alter(text):
    time.sleep(2)
    return text * 2

cProfile.run("alter('test')")
