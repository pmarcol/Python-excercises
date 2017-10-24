"""
Write a Python program to convert a string in a list.

NOTE: I assume that it should be list of 'words', not letters - ann that the separator should be up to user
"""

"""
SOLUTION:
"""

def makeList(aStr , sep = ' '):
    return aStr.split(sep)

myStr = "My-test String-of Random-Words"

print(makeList(myStr))      #['My-test', 'String-of', 'Random-Words']
print(makeList(myStr, " ")) #['My-test', 'String-of', 'Random-Words']
print(makeList(myStr, "-")) #['My',test String', 'of Random', 'Words']