"""
Write a Python program to find path refers to a file or directory when you encounter a path name.
"""

"""
SOLUTION:
"""

#see excercise 085.

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

# NOTE: Solution on source page does not seem to match the description; it implements more than is required.
# However, it does not introduce anything new regarding to what was done in previous excercises.