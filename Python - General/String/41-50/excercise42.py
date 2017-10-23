"""
Write a Python program to count repeated characters in a string.
Sample string: 'thequickbrownfoxjumpsoverthelazydog'
Expected output :
o 4
e 3
u 2
h 2
r 2
t 2
"""

"""
SOLUTION:
"""

def countReps(aStr):
    myDic = {}
    uniqueChars = set(aStr)
    for char in uniqueChars:
        if aStr.count(char) > 1:
            myDic[char] = aStr.count(char)
    return myDic

myStr = 'thequickbrownfoxjumpsoverthelazydog'
print(countReps(myStr))