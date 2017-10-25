"""
Write a Python program to get unique values from a list.
"""

"""
SOLUTION:
"""

def getUnique(aList):
    return list(set(aList))

myList1 = [1, 1, 2, 4, "test", 4, "test"]
myList2 = []

print(getUnique(myList1))   # [1, 2, 4, 'test'] not necessarily in this order
print(getUnique(myList2))   # []
