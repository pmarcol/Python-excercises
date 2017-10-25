"""
Write a Python program to convert a list of characters into a string.
"""

"""
SOLUTION:
"""

def listToString(aList):
    return ''.join(aList)

myList = ['m', 'y', 't', 'e', 's', 't', 's', 't', 'r', 'i', 'n', 'g']

print(listToString(myList))