"""
Write a Python program to strip a set of characters from a string.
"""

"""
SOLUTION:
"""

def strStrip(original, toBeRemoved):
    myTrans = str.maketrans("", "", toBeRemoved)
    return original.translate(myTrans)

myStr = "The quick brown fox jumps over the lazy dog."
myStrip = "aeiouy"

print(strStrip(myStr, myStrip))
