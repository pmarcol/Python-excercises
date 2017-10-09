"""
Write a Python program to divide a path on the extension separator.
"""

"""
SOLUTION:
"""

def divideOnExtension(thePath):
    import os
    return os.path.splitext(thePath)

for path in ['test.txt', 'filename', '/user/system/test.txt', '/', '']:
    print(divideOnExtension(path))