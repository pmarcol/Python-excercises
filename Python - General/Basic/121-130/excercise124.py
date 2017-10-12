"""
Write a Python program to check if multiple variables have the same value.

NOTE: Again, not sure what the excercise is about. Copied (and modified) the solution.
"""

"""
SOLUTION:
"""

def checkIfEqual(n1, n2, n3):
    if n1==n2==n3: return True
    return False

num1 = 5
num2 = 6
num3 = 6
num4 = 6

print(checkIfEqual(num1, num2, num3)) #False
print(checkIfEqual(num2, num3, num4)) #True
