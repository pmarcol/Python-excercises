"""
Write a Python program to make file lists from current directory using a wildcard.
"""

"""
SOLUTION:
"""

from pathlib import Path
import glob

myPath = str(Path(__file__).parent) + '\\*.*'

file_list = glob.glob(myPath)
print(file_list)