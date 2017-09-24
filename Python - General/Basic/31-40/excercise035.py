"""
 Write a Python program that will return true if the two given integer values are equal
 or their sum or difference is 5. 
"""

"""
SOLUTION:
"""

def myIndicator(a, b):
    return ((a==b) or (abs(a-b) == 5) or (a+b == 5))

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

print(myIndicator(numbersList[0],numbersList[1]))