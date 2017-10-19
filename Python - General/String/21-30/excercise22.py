"""
Write a Python program to sort a string lexicographically.
"""

"""
SOLUTION:
"""

def returnSorted(myStr):
    return ''.join(sorted(myStr, key=str.lower))

print(returnSorted("pythonTest"))