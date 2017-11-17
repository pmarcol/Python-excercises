"""
Write a Python program to check if all items of a list is equal to a given string.
"""

"""
SOLUTION:
"""

def mySol(aList, aString):
    for x in aList:
        if x != aString:
            return False
    return True

def origSol(aList, aString):
    return all(x == aString for x in aList)

color1 = ["green", "orange", "black", "white"]
color2 = ["green", "green", "green", "green"]

myStr = "green"

print(mySol(color1, myStr))      # False
print(mySol(color2, myStr))      # True
print(origSol(color1, myStr))    # False
print(origSol(color2, myStr))    # True