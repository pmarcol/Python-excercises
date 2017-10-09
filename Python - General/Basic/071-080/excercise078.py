"""
Write a Python program to find the available built-in modules.
"""

"""
SOLUTION:
"""

import sys

module_name = '\n'.join(sys.builtin_module_names)
print(module_name)