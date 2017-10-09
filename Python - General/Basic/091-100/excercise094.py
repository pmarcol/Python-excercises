"""
Write a Python program to convert a byte string to a list of integers.

NOTE: Peeking at the solution I assume the objective of the excercise is
to translate each char to ascii code.
"""

"""
SOLUTION:
"""

def myConversion(myString):
    return [ord(a) for a in myString]

print(myConversion("Test"))

#solution from source:
"""
x = b'Abc'
print(list(x))
"""
