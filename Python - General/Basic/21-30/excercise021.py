"""
Write a Python program to find whether a given number
(accept from the user) is even or odd, print out an appropriate message to the user.
"""

"""
SOLUTION:
"""

def OddOrEven(num):
    if(num%2 == 0): return "even"
    else: return "odd"

while True:
    try:
        myInt=int(input('Give a number (integer):'))
    except ValueError:
        print("Not an integer. Try again.")
        continue
    else:
        break

print("Given number (%d) is %s" %(myInt, OddOrEven(myInt)))