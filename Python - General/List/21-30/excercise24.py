"""
Write a Python program to append a list to the second list.
"""

"""
SOLUTION:
"""

def joinLists(list1, list2):
    return list1 + list2

myList1 = [1, "test", True]
myList2 = [2, "random", False]

print(joinLists(myList1, myList2)) # [1, "test", True, 2, "random", False]