"""
Write a Python program to print the following integers with '*' on the right of specified width.
"""

"""
SOLUTION:
"""

x = 3
y = 123

print("\nOriginal Number: ", x)
print("Formatted Number(right padding, width 2): "+"{:*< 3d}".format(x));
print("Original Number: ", y)
print("Formatted Number(right padding, width 6): "+"{:*< 6d}".format(y));
print()
