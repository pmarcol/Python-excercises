"""
Write a Python program to parse a string to Float or Integer.
"""

"""
SOLUTION:
"""

inputString = input('Give a number:')
try:
    myFloat=float(inputString)
except ValueError:
    print("Could not parse to float.")
else:
    print(myFloat)
try:
    myInt = int(inputString)
except ValueError:
    print("Could not parse to int.")
else:
    print(myInt)