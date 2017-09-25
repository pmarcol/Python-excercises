"""
Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).
"""

"""
SOLUTION:
"""

from math import sqrt

def calculateDistance(point1, point2):
    return sqrt( (point1[0] - point2[0])**2 + (point1[1] - point2[1])**2 )

while True:
    try:
        inputString = input('Give me 2 coordinates for first point (separated by comma):')
        elements = [x.strip() for x in inputString.split(',')]
        coordinates1 = [float(element) for element in elements]
    except ValueError:
        print('Incorrect format of input data.')
        continue
    if(len(coordinates1) != 2):
        print('You should give exactly two coordinates.')
        continue
    else:
        break

while True:
    try:
        inputString = input('Give me 2 coordinates for first point (separated by comma):')
        elements = [x.strip() for x in inputString.split(',')]
        coordinates2 = [float(element) for element in elements]
    except ValueError:
        print('Incorrect format of input data.')
        continue
    if(len(coordinates2) != 2):
        print('You should give exactly two coordinates.')
        continue
    else:
        break

print(calculateDistance(coordinates1, coordinates2))