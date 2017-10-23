"""
Write a Python program to format a number with a percentage.
"""

"""
SOLUTION:
"""

myFloat1 = 3.14159
myFloat2 = 1/3

print("{:.6%}".format(myFloat1))
print("{:.6%}".format(myFloat2))
print("{:.6%} {:.6%}".format(myFloat1, myFloat2))
