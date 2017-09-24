"""
Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s). 
Sample function : abs()
Expected Result : 
abs(number) -> number
Return the absolute value of the argument.
"""

"""
SOLUTION:
"""

import builtins

functionName = input('Give me name of a function/mmodule/type:')

try:
    print(getattr(builtins, functionName).__doc__)
except AttributeError:
    print('No such built-in object.')