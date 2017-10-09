"""
Write a Python program to get the details of math module.
"""

"""
SOLUTION:
"""

import math
import inspect     

#solution from source:   
#Sets everything to a list of math module
math_ls = dir(math) # 
print(math_ls)

#solution I found:
all_functions = inspect.getmembers(math)
only_names = [element[0] for element in all_functions]
print(only_names)