"""
Write a Python program to select an item randomly from a list.
"""

"""
SOLUTION:
"""

def getRandomElement(aList):
    alen = len(aList)
    if alen == 0:
        return None
    from random import randint
    ind = randint(0, alen - 1)
    return aList[ind]

myList1 = []
myList2 = [1, "test", True, 3.14]

#print(getRandomElement(myList1))    # None
print(getRandomElement(myList2))