"""
Write a Python program to print without newline or space.
"""

"""
SOLUTION:
"""


for i in range(0, 10):
    print('*', end="")

print("\n\n")

#for comparison: for print, it is end='\n' by default
for i in range(0, 10):
    print('*')