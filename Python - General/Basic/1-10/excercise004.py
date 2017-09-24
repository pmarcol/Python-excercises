"""
Write a Python program which accepts the radius of a circle from the user and compute the area.
Sample Output : 
r = 1.1
Area = 3.8013271108436504
"""

"""
SOLUTION:
"""

import math

pivalue = math.pi

while True:
    try:
        radius=float(input('Give radius:'))
    except ValueError:
        print("Not a number")
        continue
    else:
        break

area = pivalue*(radius**2)
print(area)