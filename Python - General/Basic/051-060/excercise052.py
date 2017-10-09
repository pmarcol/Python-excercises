from __future__ import print_function

"""
Write a Python program to print to stderr.
NOTE: from __future__ import ... must be at the beginning of the file.
"""

"""
SOLUTION:
"""


import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

eprint("test1","test2","test3",sep="***")