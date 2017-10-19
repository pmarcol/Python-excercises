"""
Write a Python program to remove a newline in Python.
NOTE: As I understand, I am supposed to remova ALL newline characters.
Solution on the source page used .rstrip() - it is assumed that newline occures at the end of the string.
"""

"""
SOLUTION:
"""

def RemoveNewline(myStr):
    return myStr.replace('\n','')

aString = "FirstLine \nSecondLine"

print(aString)
print(RemoveNewline(aString))