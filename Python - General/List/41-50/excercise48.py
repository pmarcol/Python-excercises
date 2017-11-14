"""
Write a Python program to print a nested lists (each list on a new line) using the print() function.

NOTE: Not sure what am I supposed to do. Copied the solution.
"""

"""
SOLUTION:
"""

colors = [['Red'], ['Green'], ['Black']]
print('\n'.join([str(lst) for lst in colors]))

# Note: IMO the instruction is not clear. The code takes all elements from the list and creates a string, 
# where between the elements there is specified char, in this case it is newline.