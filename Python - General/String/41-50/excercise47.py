"""
Write a Python program to lowercase first n characters in a string.
"""

"""
SOLUTION:
"""

def toLower(aStr, num):
    return aStr[:num].lower() + aStr[num:]

myStr = "MyTeStStRiNg"

print(toLower(myStr, 5))    # mytestStRiNg"
print(toLower(myStr, 100))  # myteststring
print(toLower(myStr, 0))    # MyTeStStRiNg