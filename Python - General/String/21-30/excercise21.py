"""
Write a Python function to convert a given string to all uppercase
if it contains at least 2 uppercase characters in the first 4 characters.
NOTE: ... and return the string unchanged otherwise.
"""

"""
SOLUTION:
"""

def myFunc(aString):
    subStr = aString[:4]
    #count uppercase letters
    caps = sum(1 for c in subStr if c.isupper())
    if caps >= 2:
        return aString.upper()
    else:
        return aString

myStr1 = "myTestString"
myStr2 = "MYTestString"

print(myFunc(myStr1))   #myTestString
print(myFunc(myStr2))   #MYTESTSTRING