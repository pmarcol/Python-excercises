"""
Write a Python program to shuffle and print a specified list.

NOTE: I wasn't sure about the solution, so I copied (and slightly modified) it (to create a function)
"""

"""
SOLUTION:
"""

def returnShuffled(aList):
    from random import shuffle
    shuffle(aList)
    return aList

myList1 = [7, 8, 120, 25, 44, 20, 27]
myList2 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

print(returnShuffled(myList1))
print(returnShuffled(myList2))