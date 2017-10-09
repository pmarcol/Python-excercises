"""
Write a Python program to check if a string is numeric.
"""

"""
SOLUTION:
"""

def isNumeric(inputStr):
    try:
        temp = float(inputStr)
        return True
    except ValueError:
        return False

print(isNumeric("12.66")) #True
print(isNumeric("test")) # False
print(isNumeric("t0")) # False
print(isNumeric("0")) #True