"""
Write a Python program to remove duplicates from a list.

NOTE: I achieved that by making list of set of list.
"""

"""
SOLUTION:
"""

def removeDups(aList):
    return list(set(aList))

myList = [1, 4, 2, 1, "test", 4, "test1", 4, "test"]

print(removeDups(myList)) #[1, 2, 4, "test", "test1"] not necessarily in this order