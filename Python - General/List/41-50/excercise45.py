"""
Write a Python program to convert a pair of values into a sorted unique array.

I was not sure what was I supposed to do, so the solution is copied.
"""

"""
SOLUTION:
"""

L = [(1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4), (7, 8), (9, 10)]
print("Original List: ", L)
print("Sorted Unique Data:",sorted(set().union(*L))) # * unpacks a list or tuple into position arguments
print(*L)   # (1, 2) (3, 4) (1, 2) (5, 6) (7, 8) (1, 2) (3, 4) (3, 4) (7, 8) (9, 10)