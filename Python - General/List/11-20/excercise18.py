"""
Write a Python program to generate all permutations of a list in Python.
"""

"""
SOLUTION:
"""

def perm(aList):
    from itertools import permutations
    return list(permutations(aList))

myList1 = [1, 2, 3]
myList2 = ["test", 5, True]

print(perm(myList1))
print(perm(myList2))
