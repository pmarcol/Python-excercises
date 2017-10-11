"""
Write a Python program to compute the product of a list of integers (without using for loop).
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

myList = [1,3,6]

print(myProdWithLambda(myList))
print(myProdWithoutLamda(myList))