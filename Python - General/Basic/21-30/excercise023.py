"""
Write a Python program to get the n (non-negative integer) copies of the
first 2 characters of a given string.
Return the n copies of the whole string if the length is less than 2.
"""

"""
SOLUTION:
"""

def multiplyStringNTimes(myStr, myInt):
    return myInt * myStr

while True:
    try:
        myInt=int(input('Give a number (integer):'))
    except ValueError:
        print("Not an integer. Try again.")
        continue
    if(myInt<0):
        print("The number should not be negative. Try again.")
        continue
    else:
        break

myString = input('Give a number (integer):')

print(multiplyStringNTimes(myString[:2],myInt))
