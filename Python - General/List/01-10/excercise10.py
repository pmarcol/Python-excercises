"""
Write a Python program to find the list of words that are longer than n from a given list of words. 
"""

"""
SOLUTION:
"""

def myFunc(aList, aLen):
    return [x for x in aList if len(x) > aLen]

myList = ["test", "testtes", "abc", "myString", "Python", "qwert"]

print(myFunc(myList, 5)) #["testtes", "myString", "Python"]
