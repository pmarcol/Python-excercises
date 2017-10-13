"""
Write a Python program to convert an integer to binary keep leading zeros. Go to the editor
Sample data : 50
Expected output : 00001100, 0000001100
"""

"""
SOLUTION:
"""


def TranslateToBinary(myNum):
    return '{0:08b}'.format(myNum)

myNum1 = 13
myNum2 = 1111 # If number does not fit in 8 bits, the format is expanded to required length.

print(TranslateToBinary(myNum1))
print(TranslateToBinary(myNum2))