"""
Write a Python program to generate a 3*4*6 3D array whose each element is *.
"""

"""
SOLUTION:
"""

def create3Dlist(dim1, dim2, dim3, val = '*'):
    return [[[val for i in range(dim1)] for j in range(dim2)] for k in range(dim3)]

print(create3Dlist(3, 4, 6))
