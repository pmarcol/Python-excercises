"""
Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
If the given string already ends with 'ing' then add 'ly' instead.
If the string length of the given string is less than 3, leave it unchanged.
Sample String : 'abc'
Expected Result : 'abcing' 
Sample String : 'string'
Expected Result : 'stringly'
"""

"""
SOLUTION:
"""

def myFunc(aString):
    if len(aString) < 3:
        return aString
    # I assume, that the '-ing' requirement is case sensitive
    if not(aString[-3:] == 'ing'):
        return aString + 'ing'
    else:
        return aString + 'ly'

print(myFunc("ab"))         #ab
print(myFunc("Test"))       #Testing
print(myFunc("Testing"))    #Testingly
