"""
Write a Python program to find a tuple with the smallest second index value from a list of tuples.
"""

"""
SOLUTION:
"""

def myFunc(aList):
    from operator import itemgetter
    return sorted(aList, key = itemgetter(1))[0]

x = [(4, 1), (1, 2), (6, 0), (2, -2), (1, -1, 6)]

print(myFunc(x))