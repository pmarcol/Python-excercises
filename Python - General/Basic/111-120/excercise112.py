"""
Write a Python program to remove the first item from a specified list.
"""

"""
SOLUTION:
"""

myList1 = ['test', 11, True]
myList2 = []

def removeFirst1(aList):
    return aList[1:]

def removeFirst2(aList):
    if(len(aList) > 0):
        del aList[0]
    return aList

print(removeFirst1(myList1))
print(removeFirst2(myList1))

print(removeFirst1(myList2))
print(removeFirst2(myList2))
