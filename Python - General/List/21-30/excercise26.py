"""
Write a python program to check whether two lists are circularly identical.
"""

"""
SOLUTION:
"""

def areCircularlyIdentical(list1, list2):
    if len(list1) != len(list2): return False
    supStr = ' '.join(map(str, list1*2))
    infStr = ' '.join(map(str, list2))
    return infStr in supStr

myList1 = [1, 2, 3]
myList2 = [3, 1, 2]
myList3 = [2, 1, 3]

print(areCircularlyIdentical(myList1, myList2)) # True
print(areCircularlyIdentical(myList1, myList3)) # False

test1 = ["a", "b", "c", "d"]
test2 = ["b", "c d", "a"]

print(areCircularlyIdentical(test1, test2)) # False - assumption, that lists should be of the same length is crucial here