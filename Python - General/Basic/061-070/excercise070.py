"""
Write a Python program to sort files by date.

NOTE: I wasn't sure what's the point here, so I copied (and slightly modified) the solution.
"""

"""
SOLUTION:
"""

import glob
import os

os.chdir("C:/Users/Piotrek/Downloads")
files = glob.glob("*.jpeg")
files.sort(key=os.path.getmtime)
print("\n".join(files))