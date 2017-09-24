"""Write a Python program which accepts a sequence of comma-separated numbers from user
and generate a list and a tuple with those numbers.
Sample data : 3, 5, 7, 23
Output : 
List : ['3', ' 5', ' 7', ' 23'] 
Tuple : ('3', ' 5', ' 7', ' 23')
"""

"""
SOLUTION:
"""

while True:
    try:
        inputString = input('Give me list of numbers:')
        elements = [x.strip() for x in inputString.split(',')]
        numbersList = [int(element) for element in elements]
    except ValueError:
        print('Incorrect format of input data.')
        continue
    if(len(numbersList) == 1):
        print('You should give at lest two numbers.')
        continue
    else:
        break
numbersTuple = tuple(numbersList)

print('List: %s' % (numbersList))
print('Tuple: %s' % (numbersTuple,))