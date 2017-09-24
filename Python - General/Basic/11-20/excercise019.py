"""
Write a Python program to get a new string from a given string where "Is"
has been added to the front.
If the given string already begins with "Is" then return the string unchanged.
"""

"""
SOLUTION:
"""

def addIsToString(myStr):
    if(myStr[:2] != 'Is'):
        myStr = 'Is' + myStr
    return myStr

inputString = input('Give me a string:')
print(addIsToString(inputString))