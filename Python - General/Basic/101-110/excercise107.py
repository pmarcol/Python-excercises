"""
Write a Python program to retrieve file properties.
"""

"""
SOLUTION:
"""

def fileExists(thePath):
    import pathlib
    myFile = pathlib.Path(thePath)
    return myFile.is_file()

def getFileProperties(thePath):
    import os
    if not(fileExists(thePath)):
        print("The given path does not lead to any file.")
        return
    else:
        return os.stat(thePath)

print(getFileProperties(__file__))