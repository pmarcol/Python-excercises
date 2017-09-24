"""
Write a Python program to solve (x + y) * (x + y).
Test Data : x = 4, y = 3
Expected Output : (4 + 3) ^ 2) = 49
"""

"""
SOLUTION:
"""

def myFunction(a, b):
    return (a+b)**2

while True:
    try:
        inputString = input('Give me 2 numbers (separated by comma):')
        elements = [x.strip() for x in inputString.split(',')]
        numbersList = [int(element) for element in elements]
    except ValueError:
        print('Incorrect format of input data.')
        continue
    if(len(numbersList) != 2):
        print('You should give exactly two numbers.')
        continue
    else:
        break

print(myFunction(numbersList[0],numbersList[1]))