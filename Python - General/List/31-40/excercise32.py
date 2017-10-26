"""
Write a Python program to check whether a list contains a sublist.
"""

"""
SOLUTION:
"""

def isSublist(supList, infList):
    lenSup = len(supList)
    lenInf = len(infList)
    if lenInf > lenSup: return False
    if infList == []: return True
    for i in range(lenSup - lenInf + 1):
        if supList[i:(i+lenInf)] == infList:
            return True
    return False

mySupList = [1, 2, 3, 4, 5, 6]

myInfList1 = [1, 2, 3]
myInfList2 = [2, 3, 4, 5]
myInfList3 = [4, 5, 6]
myInfList4 = []
myInfList5 = list(mySupList)
myInfList6 = [2, 4]

print(isSublist(mySupList, myInfList1)) # True
print(isSublist(mySupList, myInfList2)) # True
print(isSublist(mySupList, myInfList3)) # True
print(isSublist(mySupList, myInfList4)) # True
print(isSublist(mySupList, myInfList5)) # True
print(isSublist(mySupList, myInfList6)) # False