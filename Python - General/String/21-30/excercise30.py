"""
Write a Python program to print the following floating numbers upto 2 decimal places.
"""

"""
SOLUTION:
"""

x = 3.1415926
y = 12.9999

print('\n', x, '\n', '%.2f' % x, '\n', "{:.2f}".format(x))
print('\n', y, '\n', '%.2f' % y, '\n', "{:.2f}".format(y))