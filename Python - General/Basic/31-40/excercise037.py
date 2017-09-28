"""
Write a Python program to display your details like name, age, address in three different lines.
"""

"""
SOLUTION:
"""

import sys
import os
from pathlib import Path

abspath = Path(__file__)
toolspath = abspath.parents[3]
sys.path.append(str(toolspath / 'tools'))

from GetFromUser import GetNonNegativeInteger

def printDetails(name, address, age):
    print("Name: %s,\nAddress: %s,\nAge: %d" % (name, address, age))

#get name
myName = input("Give me yor name:")
#get address
myAddress = input("Give me your address:")
#get age
print("Let's set your age.")
myAge = GetNonNegativeInteger()

print(printDetails(myName, myAddress, myAge))