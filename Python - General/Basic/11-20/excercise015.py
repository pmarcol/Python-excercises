"""
Write a Python program to get the volume of a sphere with radius 6. EDIT: user given radius.
"""

"""
SOLUTION:
"""

import math

piVal = math.pi

while True:
    try:
        radius=float(input('Give radius:'))
    except ValueError:
        print("Not a number. Try again.")
        continue
    else:
        break

print((4/3)*piVal*(radius**3))