"""
Write a Python program to valid a IP address.

NOTE: At first I thought of some regex, but, fortunately, there is a method that validates the IP address.
NOTE2: As far as I know from the documentation, the method does not support IPv6 though.
"""

"""
SOLUTION:
"""

def validateIP(ipAdd):
    try:
        socket.inet_aton(ipAdd)
        return True
    except socket.error:
        return False

import socket
addr1 = '127.0.0.2561'
addr2 = socket.gethostbyname(socket.gethostname())
addr3 = 'test'

print(addr1, validateIP(addr1)) #False
print(addr2, validateIP(addr2)) #True
print(addr3, validateIP(addr3)) #False
