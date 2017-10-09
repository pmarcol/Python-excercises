"""
Write a Python program to get the size of a file.
"""

"""
SOLUTION:
"""

def getSizeOfFile(myPath):
    import os
    if not(os.path.isfile(myPath)):
        print("No file exists under given path.")
        return
    else: return os.path.getsize(myPath)

myPath = "C:/Users/Piotrek/Downloads/1.0.doc"
fakePath = "C:/Users/Piotrek/Downloads/test.test"

print(getSizeOfFile(myPath))
print(getSizeOfFile(fakePath))