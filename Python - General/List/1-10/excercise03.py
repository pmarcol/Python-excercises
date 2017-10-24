"""
Write a Python program to get the largest number from a list.
"""

"""
SOLUTION:
"""

def findMax1(aList):
    return max(aList)

def findMax2(aList):
    if len(aList) == 0:
        return
    max = aList[0]
    for x in aList:
        if x > max:
            max = x
    return max

myList1 = [0, -6, 10, 19, -4, 22]
myList2 =[]

print(findMax1(myList1)) #22
print(findMax2(myList1)) #22

#print(findMax1(myList2)) #Error
print(findMax2(myList2)) #None