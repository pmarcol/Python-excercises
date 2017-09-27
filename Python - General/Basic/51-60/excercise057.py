"""
Write a program to get execution time for a Python method.
"""

"""
SOLUTION:
"""

import time

def alter(text):
    time.sleep(2)
    return text * 2

time_start = time.time()

alter("test")

print("execution of the function took", time.time() - time_start, "seconds")