"""
Write a Python program to calculate the sum of three given numbers,
if the values are equal then return thrice of their sum.
"""

"""
SOLUTION:
"""

def specialSum(num1, num2, num3):
    result = num1 + num2 + num3
    if(num1==num2==num3):
        result *= 3
    return result

while True:
    try:
        inputString = input('Give me list of 3 numbers:')
        elements = [x.strip() for x in inputString.split(',')]
        numbersList = [int(element) for element in elements]
    except ValueError:
        print('Incorrect format of input data.')
        continue
    if(len(numbersList) != 3):
        print('You should give exactly three numbers.')
        continue
    else:
        break

print(specialSum(numbersList[0],numbersList[1],numbersList[2]))