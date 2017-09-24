"""
Write a Python program to get the Python version you are using.
"""

"""
SOLUTION:
"""

import sys
version = sys.version_info
print("%d.%d.%d" % (version.major, version.minor, version.micro))