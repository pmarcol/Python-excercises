"""
Write a Python program to get the smallest number from a list.
"""

"""
SOLUTION:
"""

def findMin1(aList):
    return min(aList)

def findMin2(aList):
    if len(aList) == 0:
        return
    min = aList[0]
    for x in aList:
        if x < min:
            min = x
    return min

myList1 = [0, -6, 10, 19, -4, 22]
myList2 =[]

print(findMin1(myList1)) # -6
print(findMin2(myList1)) # -6

#print(findMax1(myList2)) #Error
print(findMin2(myList2)) #None