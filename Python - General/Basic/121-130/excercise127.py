"""
Write a Python program to check if an integer fits in 64 bits.
"""

"""
SOLUTION:
"""

def checkIfFitsIn64Bits(num):
    if num.bit_length() < 64 : return True
    return False

int1 = 5
int2 = 2**64 + 1

print(checkIfFitsIn64Bits(int1))
print(checkIfFitsIn64Bits(int2))
