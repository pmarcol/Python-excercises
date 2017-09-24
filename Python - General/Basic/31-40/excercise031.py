"""
Write a Python program to compute the greatest common divisor (GCD) of two positive integers.
"""

"""
SOLUTION:
"""

#Euclidean Algorithm:
def getGCD(a,b):
    x = max(a, b)
    y = min(a, b)
    if(x%y == 0): return y
    temp = 0
    rem = y
    nextrem = x - (x//y)*y
    while(nextrem > 0):
        temp = rem
        rem = nextrem
        nextrem = temp - (temp//nextrem)*nextrem
    
    return rem

while True:
    try:
        myInt1=int(input('Give first number (positive integer):'))
    except ValueError:
        print("Not an integer. Try again.")
        continue
    if(myInt1<0):
        print("The number should not be negative. Try again.")
        continue
    else:
        break

while True:
    try:
        myInt2=int(input('Give first number (positive integer):'))
    except ValueError:
        print("Not an integer. Try again.")
        continue
    if(myInt2<0):
        print("The number should not be negative. Try again.")
        continue
    else:
        break

print("GCD of %d and %d is %d." % (myInt1,myInt2,getGCD(myInt1,myInt2)))