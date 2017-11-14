"""
Write a Python program to find missing and additional values in two lists.
Sample data : Missing values in second list: b,a,c
Additional values in second list: g,h
"""

"""
SOLUTION:
"""

def trackDiffs(origList, othList):
    missing = list(set(origList).difference(set(othList)))
    additional = list(set(othList).difference(set(origList)))
    print("Missing: " + str(missing) + "\nAdditional: " + str(additional))
    return

list1 = ['a','b','c','d','e','f']
list2 = ['d','e','f','g','h']

trackDiffs(list1, list2)