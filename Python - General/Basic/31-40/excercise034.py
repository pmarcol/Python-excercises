"""
Write a Python program to sum of two given integers.
However, if the sum is between 15 to 20 it will return 20
"""

"""
SOLUTION:
"""

def specialSum(a, b):
    output = a + b
    if(15<= output <= 20): output = 20
    return output

while True:
    try:
        inputString = input('Give me 2 numbers (separated by comma):')
        elements = [x.strip() for x in inputString.split(',')]
        numbersList = [int(element) for element in elements]
    except ValueError:
        print('Incorrect format of input data.')
        continue
    if(len(numbersList) != 2):
        print('You should give exactly three numbers.')
        continue
    else:
        break

print(specialSum(numbersList[0],numbersList[1]))