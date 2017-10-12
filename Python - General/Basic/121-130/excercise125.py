"""
Write a Python program to sum of all counts in a collections?

NOTE: Okay, I got it wrong. I thought it is about summing the values in a list. But it's not. (Copied from the source)
"""

"""
SOLUTION:
"""

import collections
num = [2,2,4,6,6,8,6,10,4]
print(sum(collections.Counter(num).values()))

# Note: it seems that it just counts the elements of the list.
# Why not len(list) then?