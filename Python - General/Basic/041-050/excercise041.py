"""
Write a Python program to check whether a file exists.
"""

"""
SOLUTION:
"""

from pathlib import Path

def fileExists(filePath):
    my_file = Path(filePath)
    return my_file.is_file()

print(fileExists("test/file.txt")) #False
print(fileExists("E:/Python/Python-excercises/Python - General/Basic/41-50/excercise041.py")) #True