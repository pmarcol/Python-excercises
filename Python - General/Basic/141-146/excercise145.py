"""
Write a Python program to test if a variable is a list or tuple or a set.

NOTE: Correct excercise instructions can be found in the solution subpage.
"""

"""
SOLUTION:
"""

def determineType(obj):
    if isinstance(obj, (list, tuple, set)):
        return True
    return False

print(determineType([25]), determineType((1,'test',True)), determineType(set(['foo', 'bar'])), determineType('test'), sep=', ') #True, True, True, False