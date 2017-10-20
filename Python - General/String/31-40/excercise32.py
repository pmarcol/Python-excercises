"""
Write a Python program to print the following floating numbers with no decimal places.
"""

"""
SOLUTION:
"""

x = 3.1415926
y = -12.9999

print('\n', x, '\n', '%+.0f' % x, '\n', "{:+.0f}".format(x))
print('\n', y, '\n', '%+.0f' % y, '\n', "{:+.0f}".format(y))