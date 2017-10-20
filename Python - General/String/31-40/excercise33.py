"""
Write a Python program to print the following integers with zeros on the left of specified width.
"""

"""
SOLUTION:
"""

x = 3
y = 123

print('\n', x, '\n', '%08d' % x, '\n', "{:08d}".format(x))
print('\n', y, '\n', '%08d' % y, '\n', "{:08d}".format(y))
print()
#Nice formatting - with padding
print("{:0>8d}".format(x))
print("{:0<8d}".format(y))