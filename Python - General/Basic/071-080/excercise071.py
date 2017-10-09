"""
Write a Python program to get a directory listing, sorted by creation date.
"""

"""
SOLUTION:
"""

import os

def unixTimestampToDatetime(ts):
    import datetime
    out = datetime.datetime.fromtimestamp(ts)
    return out

myDir = "C:/Users/Piotrek/Downloads"

os.chdir(myDir)
dirs = [o for o in os.listdir() if os.path.isdir(os.path.join(os.curdir, o))]
dirs.sort(key=os.path.getmtime)
print("\n".join(dirs))
"""
for o in dirs:
    print(o, ':', unixTimestampToDatetime(os.path.getmtime(o)))
"""