"""
Write a Python program to print the numbers of a specified list after removing even numbers from it.
"""

"""
SOLUTION:
"""

def returnNotEven(aList):
    return [x for x in aList if x%2 != 0]

myList = [7, 8, 120, 25, 44, 20, 27]

print(returnNotEven(myList)) # [7, 25, 27]