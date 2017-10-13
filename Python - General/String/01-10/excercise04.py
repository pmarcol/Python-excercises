"""
Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$',
except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t'
"""

"""
SOLUTION:
"""

def myFunc(aString):
    if len(aString) < 2:
        return aString
    c = aString[0]
    out = c +  (aString[1:]).replace(c, '$')
    return out
    
print(myFunc('test'))
print(myFunc('aa'))
print(myFunc('t'))
print(myFunc('restart'))