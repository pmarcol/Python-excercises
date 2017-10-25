"""
Write a Python program to find the index of an item in a specified list.
"""

"""
SOLUTION:
"""

def findInList(el, aList):
    if not el in aList:
        return None
    return aList.index(el)

myList = [1, "test", True, 3.14]

print(findInList("test", myList))   # 2
print(findInList(False, myList))    # None