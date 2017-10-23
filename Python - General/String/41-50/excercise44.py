"""
Write a Python program to print the index of the character in a string.
Sample string: w3resource
Expected output:
Current character w position at 0
Current character 3 position at 1
Current character r position at 2
- - - - - - - - - - - - - - - - - - - - - - - - -
Current character c position at 8
Current character e position at 9
"""

"""
SOLUTION:
"""

def listCharsWithIndexes(aStr):
    for char, index in enumerate(aStr):
        print(char, index)

myStr = "My test String 1"
listCharsWithIndexes(myStr)