"""
Write a Python program to check if a string contains all letters of the alphabet.
"""

"""
SOLUTION:
"""

def myCheck(aStr):
    import string
    lowStr = aStr.lower()
    alphabet = set(string.ascii_lowercase)
    return set(lowStr) >= alphabet

myStr1 = "myTestString"
myStr2 = "qwErtyUiopaSdfgHjklzXcvbnM"

print(myCheck(myStr1)) #False
print(myCheck(myStr2)) #True
