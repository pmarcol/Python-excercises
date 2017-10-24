"""
Write a Python program to swap comma and dot in a string.
Sample string: "32.054,23"
Expected Output: "32,054.23"
"""

"""
SOLUTION:
"""

def swapDotsAndCommas(aStr):
    myTrans = str.maketrans('.,', ',.')
    return aStr.translate(myTrans)

myStr1 = "..,,,.,,..."
myStr2 = "32,054.23"

print(swapDotsAndCommas(myStr1))    # ,,...,..,,,
print(swapDotsAndCommas(myStr2))    # 32.054,23