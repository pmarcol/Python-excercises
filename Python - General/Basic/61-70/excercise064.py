"""
Write a Python program to get file creation and modification date/times.
"""

"""
SOLUTION:
"""

import os
from pathlib import Path

def unixTimestampToDatetime(ts):
    import datetime
    out = datetime.datetime.fromtimestamp(ts)
    return out

def fileExists(filePath):
    my_file = Path(filePath)
    return my_file.is_file()

def getCreationDate(myFile):
    if(not(fileExists(myFile))):
        print("File does not exist.")
        return
    else:
        return os.path.getctime(myFile)

def getModificationDate(myFile):
    if(not(fileExists(myFile))):
        print("File does not exist.")
        return
    else:
        return os.path.getmtime(myFile)

myFile = os.path.realpath(__file__)

print("Creation time: %s" % unixTimestampToDatetime(getCreationDate(myFile)))
print("Modification time: %s" % unixTimestampToDatetime(getModificationDate(myFile)))