"""
Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
Sample value of n is 5 
Expected Result : 615
"""

"""
SOLUTION:
"""

while True:
    try:
        inputString = input('Give me an integer:')
        myNumber1 = int(inputString)
        myNumber2 = int(2*inputString)
        myNumber3 = int(3*inputString)
    except ValueError:
        print('Make sure you are giving an integer. Try again:')
        continue
    else:
        break

result = myNumber1 + myNumber2 + myNumber3
print('The result is: %d' % result)