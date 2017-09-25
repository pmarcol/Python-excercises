"""
Write a Python program to find out the number of CPUs using.
"""

"""
SOLUTION:
"""

from multiprocessing import cpu_count

print(cpu_count())