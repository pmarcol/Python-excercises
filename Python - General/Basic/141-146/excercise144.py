"""
Write a Python program to check if variable is of integer or string.
"""

"""
SOLUTION:
"""

def determineType(obj):
    if isinstance(obj, (int, str)):
        return True
    return False

print(determineType(25), determineType([]), determineType('test'), sep=', ') #True, False, True