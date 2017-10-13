"""
Write a Python program to remove the nth index character from a nonempty string.
"""

"""
SOLUTION:
"""

def myFunc(aString, ind):
    # indexing from 0 ofc
    if len(aString) <= ind:
        print("Pointed index is larger than the string's length")
        return
    return aString[:ind] + aString[(ind+1):]

print(myFunc("myTestString", 4))    # myTetString
print(myFunc("test", 4))            # Error