"""
Write a Python program to add leading zeroes to a string.
"""

"""
SOLUTION:
"""

def addLeadingZerosFactory(numberOfZeros):
    def AddZeros(myStr):
        return numberOfZeros*'0' + myStr
    return AddZeros

add3zeros = addLeadingZerosFactory(3)

print(add3zeros('test'))

#Note: Nice! I used an enclosure here.