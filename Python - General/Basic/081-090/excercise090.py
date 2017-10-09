"""
Write a Python program to create a copy of its own source code.

NOTE: I have no idea what this excercise is about. I copied the solution.
"""

"""
SOLUTION:
"""

#original solution:
#print((lambda str='print(lambda str=%r: (str %% str))()': (str % str))())

#solution from comment:

import sys

file = open(sys.argv[0],'r')
l = file.readline()
while(l!=''):
    print(l,end='')
    l = file.readline()
