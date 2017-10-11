"""
Write a Python program to prove that two string variables of same value point same memory location.
"""

"""
SOLUTION:
"""

str1 = "test"
str2 = "test"

print(id(str1)==id(str2))
