"""
Write a python program to access environment variables.
"""

"""
SOLUTION:
"""

import os

myvar = os.environ

for item in myvar:
    print(item, ':', myvar[item])
