"""
Write a Python script that takes input from the user
and displays that input back in upper and lower cases.
"""

"""
SOLUTION:
"""

def printUpperAndLower(myStr):
    print("Upper: " + myStr.upper())
    print("Lower: " + myStr.lower())
    return

myString = input("Give me a string:")
printUpperAndLower(myString)
#printUpperAndLower("TesTsTrINg12*")