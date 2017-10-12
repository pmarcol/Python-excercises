"""
Write a Python program to determine if variable is defined or not.

NOTE: Not sure what it is about. Copied.
"""

"""
SOLUTION:
"""

#From source page:
"""
try:
  x = 1
except NameError:
  print("Variable is not defined....!")
else:
  print("Variable is defined.")
try:
  y
except NameError:
  print("Variable is not defined....!")
else:
  print("Variable is defined.")
"""

#From stackoverflow:
"""
if 'myVar' in locals():
      # myVar exists.
To check the existence of a global variable:

if 'myVar' in globals():
  # myVar exists.
To check if an object has an attribute:

if hasattr(obj, 'attr_name'):
"""

