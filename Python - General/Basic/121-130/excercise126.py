"""
Write a Python program to get the actual module object for a given object.
"""

"""
SOLUTION:
"""

from inspect import getmodule
from math import sqrt
from sklearn import svm
print(getmodule(sqrt))
print(getmodule(svm))