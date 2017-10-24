"""
Write a Python program to split a string on the last occurrence of the delimiter.
"""

"""
SOLUTION:
"""

def mySplit(aStr, aDel):
    return aStr.rsplit(aDel,1)

myStr = "test. String.with sep"

print(mySplit(myStr, '.'))  #['test. String', 'with sep']
print(mySplit(myStr, ' '))  #['test. String.with', 'sep']
print(mySplit(myStr, '!'))  #['test. String.with sep']