"""
Write a Python program to compute the future value of a specified principal amount,
rate of interest, and a number of years.
Test Data : amt = 10000, int = 3.5, years = 7
Expected Output : 12722.79
"""

"""
SOLUTION:
"""

def calculateFutureValue(origAmount, intRate, numberOfYears):
    factor = 1 + (intRate/100)
    return origAmount * ((factor)**numberOfYears)

while True:
    try:
        amt=float(input('Give original amount:'))
    except ValueError:
        print("Not a number. Try again.")
        continue
    if(amt < 0):
        print("Amount should not be negative. Try again.")
        continue
    else:
        break

while True:
    try:
        rate=float(input('Give interest rate:'))
    except ValueError:
        print("Not a number. Try again.")
        continue
    if(rate < 0):
        print("Interest rate should not be negative. Try again.")
        continue
    else:
        break

while True:
    try:
        yrs=int(input('Give number of years:'))
    except ValueError:
        print("Not an integer. Try again.")
        continue
    if(yrs < 0):
        print("Number of years should not be negative. Try again.")
        continue
    else:
        break

print(calculateFutureValue(amt, rate, yrs))