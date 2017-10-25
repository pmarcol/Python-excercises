"""
Write a Python program to get the frequency of the elements in a list.
"""

"""
SOLUTION:
"""

def getFreq(aList):
    dic = {}
    for el in set(aList):
        dic[el] = aList.count(el)
    return dic

myList = [10,10,10,10,20,20,20,20,40,40,50,50,30]

print(getFreq(myList)) # {10: 4, 20: 4, 30: 1, 40: 2, 50: 2} not necessarily in this order