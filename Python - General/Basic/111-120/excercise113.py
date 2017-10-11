"""
Write a Python program to input a number, if it is not a number generate an error message.

NOTE: Ok, so my understanding of this excercise is slightly different from what can be found in the official solution.
I understand, that I'm supposed to write a function, that returns True/prints some message if input object is a number,
and throws an exception if it's not.
Here's my approach.
"""

"""
SOLUTION:
"""

def identifyNumber(inp):
    if (not(isinstance(inp, (int, float))) or isinstance(inp, bool)):
        raise TypeError('Input object is not a number.')
    else:
        print("Input object is a number.")
    return

myInt = int('5')
myFloat = float('3.14')
myString = 'test'
myStringNum = '5'
myBool = True

myList = [myInt, myFloat, myString, myStringNum, myBool]

for obj in myList:
    try:
        print(identifyNumber(obj))
    except TypeError as err:
        print(str(err))