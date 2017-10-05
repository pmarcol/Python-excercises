"""
Write a Python program to check if a file path is a file or a directory.
"""

"""
SOLUTION:
"""

def dirOrPath(thePath):
    import os
    if(os.path.isdir(thePath)): return "dir"
    elif(os.path.isfile(thePath)): return "file"
    else: return
        

dirPath = "C:/Users/Piotrek/Downloads"
print(dirOrPath(dirPath))
#dir
filePath = "C:/Users/Piotrek/Downloads/1.0.doc"
print(dirOrPath(filePath))
#file
nonePath = "C:/Users/Piotrek/Downloads/test.test"
print(dirOrPath(nonePath))
#None
