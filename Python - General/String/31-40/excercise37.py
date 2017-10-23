"""
Write a Python program to display a number in left, right and center aligned of width 10.
"""

"""
SOLUTION:
"""

myNum = 123

print("{:<10}".format(myNum))
print("{:>10}".format(myNum))
print("{:^10}".format(myNum))