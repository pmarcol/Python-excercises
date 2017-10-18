"""
Write a Python function to reverses a string if it's length is a multiple of 4.

NOTE: ... and returns the string itself otherwise? I assumed so in my implementation.
"""

"""
SOLUTION:
"""

def mySpecialFunc(myStr):
    alen = len(myStr)
    if alen%4 != 0:
        return myStr
    return myStr[::-1]
    #return ''.join(reversed(myStr))

print(mySpecialFunc("MyTestString"))    #gnirtStseTyM
print(mySpecialFunc("abcde"))           #abcde