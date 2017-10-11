"""
Write a Python program to filter the positive numbers from a list.
"""

"""
SOLUTION:
"""

def filterPositive(aList):
    #Note: no type checking
    return list(filter(lambda x: (x>0), aList))

myList = [-1,0,1,0.44, -6.4]

print(filterPositive(myList))