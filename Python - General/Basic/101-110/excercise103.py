"""
Write a Python program to extract the filename from a given path.
"""

"""
SOLUTION:
"""

def getFilename(thePath):
    import os
    return os.path.basename(thePath)

myPath = "C:/Users/Piotrek/Downloads/clipboard-list-flat.png"
myFakePath = "T:/test/test.txt"
print(getFilename(myPath))
print(getFilename(myFakePath))