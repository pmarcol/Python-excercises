"""
Write a Python program to test whether a number is within 100 of 1000 or 2000.
"""

"""
SOLUTION:
"""

def closeTo1000or2000(num):
    return(min(abs(1000-num), abs(2000-num))<=100)

while True:
    try:
        myInt=int(input('Give a number (integer):'))
    except ValueError:
        print("Not an integer. Try again.")
        continue
    else:
        break

print('%d is within 100 of 1000 or 2000: %s' % (myInt, closeTo1000or2000(myInt)))