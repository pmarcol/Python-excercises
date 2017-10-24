"""
Write a Python program to check a list is empty or not.
"""

"""
SOLUTION:
"""

def isEmpty(aList):
    return not(bool(aList))

myList1 = [1]
myList2 = []

print(isEmpty(myList1)) # False
print(isEmpty(myList2)) # True