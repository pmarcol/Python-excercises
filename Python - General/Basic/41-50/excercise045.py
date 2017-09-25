"""
Write a python program to call an external command in Python.
"""

"""
SOLUTION:
"""

from subprocess import call
call('dir', shell=True)