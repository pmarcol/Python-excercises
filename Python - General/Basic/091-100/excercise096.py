"""
Write a Python program to print the current call stack.
"""

"""
SOLUTION:
"""

import traceback

def f():
    g()

def g():
    for line in traceback.format_stack():
        print(line.strip())

f()
g()