"""
Write a Python program to count the number of characters (character frequency) in a string.
Sample String : google.com'
Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
"""

"""
SOLUTION:
"""

def myFunc(aString):
    myDict = {}
    chars = set(aString)
    for c in chars:
        myDict[c] = aString.count(c)
    return myDict

print(myFunc('test'))