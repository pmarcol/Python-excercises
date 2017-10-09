"""
Write a Python program to get OS name, platform and release information.
"""

"""
SOLUTION:
"""

import platform
import os
print(os.name)
print(platform.system())
print(platform.release())