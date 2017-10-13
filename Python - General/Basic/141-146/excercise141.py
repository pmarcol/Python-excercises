"""
Write a python program to convert decimal to hexadecimal.
Sample decimal number: 30, 4
Expected output: 1e, 04 
"""

"""
SOLUTION:
"""

def IntToHex(myNum):
    return format(myNum,'02x')

print(IntToHex(5))
print(IntToHex(55))
print(IntToHex(248))