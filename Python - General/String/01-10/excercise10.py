"""
Write a Python program to change a given string to a new string where the first and last chars have been exchanged.
"""

"""
SOLUTION:
"""

def myFunc(aString):
    if len(aString) < 2:
        return aString
    return aString[-1] + aString[1:-1] + aString[0]

print(myFunc(""))       # <empty>
print(myFunc("a"))      # a
print(myFunc("ab"))     # ba
print(myFunc("abc"))    # cba