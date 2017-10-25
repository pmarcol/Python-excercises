"""
Write a Python function that takes two lists and returns True if they have at least one common member. 
"""

"""
SOLUTION:
"""

def haveCommon(list1, list2):
    return bool( set(list1) & set(list2) )

myList1 = [1,2,3]
myList2 = [3,4,5]
myList3 = [5,6,7]

print(haveCommon(myList1, myList2)) # True
print(haveCommon(myList2, myList3)) # True
print(haveCommon(myList1, myList3)) # False
print(haveCommon([], myList1))      # False