"""
Write a Python program to calculate the hypotenuse of a right angled triangle.
"""

"""
SOLUTION:
"""

from math import sqrt
import sys
import os
from pathlib import Path

abspath = Path(__file__)
toolspath = abspath.parents[3]

sys.path.append(str(toolspath / 'tools'))

from GetFromUser import GetListOfFloats

def getTheHypotenuse(cath1, cath2):
    hyp = sqrt(cath1**2 + cath2**2)
    return hyp

#Get the cathetuses
print("Give me the cathetuses:")
while True:
    cath = GetListOfFloats()
    if(len(cath) != 2):
        print("You should give exactly two values. Try again.")
        continue
    elif(min(cath) <= 0):
        print("Both values should be positive. Try again.")
        continue
    else:
        break

print("If first cathetus has length %f and the second has length %f, then hypotenuse has length %f." 
% (cath[0], cath[1], getTheHypotenuse(cath[0],cath[1])))