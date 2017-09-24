"""
Write a Python program that will accept the base and height of a triangle and compute the area
"""

"""
SOLUTION:
"""

def calculateArea(base, height):
    return 0.5*base*height

while True:
    try:
        base=float(input('Give base:'))
    except ValueError:
        print("Not a number. Try again.")
        continue
    if(base < 0):
        print("Base should not be negative. Try again.")
        continue
    else:
        break

while True:
    try:
        height=float(input('Give height:'))
    except ValueError:
        print("Not a number. Try again.")
        continue
    if(height < 0):
        print("Height should not be negative. Try again.")
        continue
    else:
        break

print("Area of the triangle: %s" % calculateArea(base,height))