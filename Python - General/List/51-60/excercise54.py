"""
Write a Python program to concatenate elements of a list.
"""

"""
SOLUTION:
"""

def myFunc(aList):
    return ''.join([str(x) for x in aList])

myList = [1, 3.14, True, [1, 2, 3]]
print(myFunc(myList)) # 13.14True[1, 2, 3]