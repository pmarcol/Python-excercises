"""
Write a Python program to determine if the python shell is executing in 32bit or 64bit mode on operating system.

NOTE: See excercise 042
"""

"""
SOLUTION:
"""

# Solution from the source
import struct
print(struct.calcsize("P") * 8)

# I like this one more
import platform
print(platform.architecture())
print(platform.architecture()[0])