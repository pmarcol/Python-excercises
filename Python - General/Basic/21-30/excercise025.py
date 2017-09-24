"""
Write a Python program to check whether a specified value is contained in a group of values.
Test Data : 
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False
"""

"""
SOLUTION:
"""

def listContainsElement(myList, myElement):
    return (myList.count(myElement) > 0)

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

while True:
    try:
        myInt=int(input('Give a number (integer):'))
    except ValueError:
        print("Not an integer. Try again.")
        continue
    else:
        break

print("The list: %s contains %d: %s" % (numbersList, myInt, listContainsElement(numbersList,myInt)))