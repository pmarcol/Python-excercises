"""
Write a Python program to count the number 4 in a given list.
"""

"""
SOLUTION:
"""

def countFours(myList):
    return myList.count(4)

while True:
    try:
        inputString = input('Give me list of numbers:')
        elements = [x.strip() for x in inputString.split(',')]
        numbersList = [int(element) for element in elements]
    except ValueError:
        print('Incorrect format of input data.')
        continue
    else:
        break

print("Given list contains %d 4's." % (countFours(numbersList)))