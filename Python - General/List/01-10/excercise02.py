"""
Write a Python program to multiplies all the items in a list.

NOTE: See excercise 115 from Basic section.
"""

"""
SOLUTION:
"""

from functools import reduce

def myProdWithLambda(aList):
    return reduce(lambda x, y : x*y, aList)

def myProdWithoutLamda(aList):
    from operator import mul
    return reduce(mul, aList)

def myProdWithLoop(aList):
    out = 1
    for x in aList:
        out *= x
    return out

myList = [1,3,6]

print(myProdWithLambda(myList))
print(myProdWithoutLamda(myList))
print(myProdWithLoop(myList))