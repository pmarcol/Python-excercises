"""
Write a Python program to flatten a shallow list.
"""

"""
SOLUTION:
"""

def flatten(aList):
    import itertools
    flatList = list(itertools.chain(*aList))
    return flatList

myList = [[2,4,3],[1,5,6], [9], [7,9,0]]

print(flatten(myList)) # [2, 4, 3, 1, 5, 6, 9, 7, 9, 0]