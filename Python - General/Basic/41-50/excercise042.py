"""
Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS.
"""

"""
SOLUTION:
"""

# For 32 bit it will return 32 and for 64 bit it will return 64
# Solution from the source
import struct
print(struct.calcsize("P") * 8)

# I like this one more
import platform
print(platform.architecture())
print(platform.architecture()[0])