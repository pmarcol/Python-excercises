"""
Write a Python program to check if the nth element exists in a given list.

Note: Sample solution from the source page is not even worth looking at.
Totally not what it was about (or I totally don't understand it)
"""

"""
SOLUTION:
"""

# approach 1: just check the length
def checkNth1(aList, num):
    if len(aList) - 1 < num:
        return False
    return True

# approach 2: more generic, try to get the element with given index
def checkNth2(aList, num):
    try:
        temp = aList[num]
    except IndexError:
        return False
    return True

myList = [0, 1, 2]
print(checkNth1(myList, 3)) # False
print(checkNth1(myList, 2)) # True
print(checkNth2(myList, 3)) # False
print(checkNth2(myList, 2)) # True
