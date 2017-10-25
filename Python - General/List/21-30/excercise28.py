"""
Write a Python program to find the second largest number in a list.
"""

"""
SOLUTION:
"""

def findSecondGreatest(aList):
    if len(aList) < 2:
        return
    return sorted(aList)[-2]

myList1 = [3.14, 7, -3, 12, -8]
myList2 = [1, 1, 4, 3]
myList3 = [1]

print(findSecondGreatest(myList1))  # 7
print(findSecondGreatest(myList2))  # 3
print(findSecondGreatest(myList3))  # None 