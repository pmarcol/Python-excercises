"""
Write a Python program to sum all the items in a list.

NOTE: No checking if items in a list are numbers.
"""

"""
SOLUTION:
"""

def sumList(aList):
    out = 0
    for x in aList:
        out += x
    return out

myList1 = [1,4,-10]

print(sumList(myList1)) # -5