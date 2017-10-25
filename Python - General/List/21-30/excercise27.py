"""
Write a Python program to find the second smallest number in a list.
"""

"""
SOLUTION:
"""

def findSecondSmallest(aList):
    if len(aList) < 2:
        return
    return sorted(aList)[1]

myList1 = [3.14, 7, -3, 12, -8]
myList2 = [1, 1, 4, 3]
myList3 = [1]

print(findSecondSmallest(myList1))  # -3
print(findSecondSmallest(myList2))  # 1
print(findSecondSmallest(myList3))  # None 