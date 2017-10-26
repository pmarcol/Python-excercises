"""
Write a Python program to count the number of elements in a list within a specified range.
"""

"""
SOLUTION:
"""

def countInRange(aList, rBottom, rTop):
    return sum([1 for x in aList if rBottom <= x <= rTop])

myList = [-1, 4, 8, 2, 0, -3, 7, 1, 5]
bottom = 1
top = 5

print(countInRange(myList, bottom, top)) # 4
