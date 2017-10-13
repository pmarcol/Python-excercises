"""
Write a Python program to convert true to 1 and false to 0.
"""

"""
SOLUTION:
"""

def boolToInt(myBool):
    if not(isinstance(myBool, bool)):
        return
    if myBool:
        return 1
    elif not(myBool):
        return 0

print(boolToInt(True))      #1
print(boolToInt(False))     #0
print(boolToInt(1))         #None
print(boolToInt('test'))    #None