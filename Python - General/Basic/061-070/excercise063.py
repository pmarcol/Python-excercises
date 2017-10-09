"""
Write a Python program to get an absolute file path.

NOTE: Not sure what I am supposed to do.
However, looking at the solution on source page, I assume the excercise is about using os.path.abspath function.
"""

"""
SOLUTION:
"""

def absolute_file_path(path_fname):
        import os
        return os.path.abspath(path_fname)

print(absolute_file_path("imaginaryFile.py"))
#out>> h:\python\Course\Python-excercises\imaginaryFile.py
