"""
Write a Python program to get the name of the host on which the routine is running.
"""

"""
SOLUTION:
"""

import socket

print(socket.gethostname())