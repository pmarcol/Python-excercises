"""
 Write a Python program to create a histogram from a given list of integers.
"""

"""
SOLUTION:
"""

def histogram(myList):
    output = ''
    for n in myList:
        times = n
        bar = ''
        while( times > 0 ):
            bar += '*'
            times = times - 1
        if(output != ''):
            output += '\n'
        output += bar
    return output

while True:
    try:
        inputString = input('Give me list of numbers (nonnegative integers):')
        elements = [x.strip() for x in inputString.split(',')]
        numbersList = [int(element) for element in elements]
    except ValueError:
        print('Incorrect format of input data.')
        continue
    if(min(numbersList) < 0):
        print("All integers should be nonegative. Try again.")
        continue
    else:
        break


print(histogram(numbersList))