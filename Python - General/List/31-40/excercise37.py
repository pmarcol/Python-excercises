"""
Write a Python program to find common items from two lists.
"""

"""
SOLUTION:
"""

def findCommons(aList1, aList2):
    return list(set(aList1) & set(aList2))

myList1 = [1, 2, 3, 'test', 'test1']
myList2 = [3, 4, 5, 'test1', 'test2', 3.14]

print(findCommons(myList1, myList2)) # [3, 'test1'] not necessarily in this order

# NOTE: I tried to test the function with lists with bool values; it turns out, that Python interprets them as ints (1 and 0);
# thus, if you add True to the second list, there will be 1 in returned list (because 1 is in the first list). Interesting.
