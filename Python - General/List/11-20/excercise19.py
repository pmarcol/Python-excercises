"""
Write a Python program to get the difference between the two lists.

NOTE: Original solution makes just sets of both lists and then returns listed difference between the sets.
My understanding is different: I would not make sets, but instead, I would remove all elements occuring in list2 from list1.
And if there are remaining the same values in list1 - leave them as they are.
"""

"""
SOLUTION:
"""

def myFunc(list1, list2):
    for x in list2:
        for i in range(len(list1)):
            if x == list1[i]:
                del list1[i]
                break
    return list1

myList1 = [1, 2, 2, 3, 3, 3, 4]
myList2 = [1, 2, 3, 4]

print(myFunc(myList1, myList2)) # [2, 3, 3]