"""
Write a Python program to get the users environment.
"""

"""
SOLUTION:
"""

#See excercise 053

import os

myvar = os.environ

for item in myvar:
    print(item, ':', myvar[item])