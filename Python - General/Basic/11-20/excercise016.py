"""
Write a Python program to get the difference between a given number and 17,
if the number is greater than 17 return double the absolute difference.
"""

"""
SOLUTION:
"""

def difference17(num):
    if(num>17):
        return 2*abs(17-num)
    else:
        return abs(17-num)

while True:
    try:
        myInt=int(input('Give a number (integer):'))
    except ValueError:
        print("Not an integer. Try again.")
        continue
    else:
        break

print(difference17(myInt))