"""
Write a Python program access the index of a list.
"""

"""
SOLUTION:
"""

def myFunc(aList):
    myDic = {}
    for i in range(len(aList)):
        myDic[i] = aList[i]
    return myDic

myList = [1, True, "test", (1, 2), [1,2]]

dic = myFunc(myList)

for k in dic.keys():
    print(k, ':', dic[k])