"""
Write a Python program to find files and skip directories of a given directory.

NOTE: See excercise 049.
"""

"""
SOLUTION:
"""

from os import listdir, path
from os.path import isfile, join

def listFiles(myPath):
    if(not(path.isdir(myPath))):
        print("Such path does not exist or it does not lead to directory.")
        return
    else:
        onlyfiles = [f for f in listdir(myPath) if isfile(join(myPath, f))]
        if (len(onlyfiles)==0):
            print ("No files here.")
            return
        else:
            print(onlyfiles)
            return

listFiles("C:/Users/pmarcol/Downloads")