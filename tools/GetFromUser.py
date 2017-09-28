def GetInteger():
    while True:
        try:
            myInt=int(input('Give a number (integer):'))
        except ValueError:
            print("Not an integer. Try again.")
            continue
        else:
            break
    return myInt

def GetPositiveInteger():
    while True:
        try:
            myInt=int(input('Give a number (positive integer):'))
        except ValueError:
            print("Not an integer. Try again.")
            continue
        if(myInt<=0):
            print("The number should be positive. Try Again.")
            continue
        else:
            break
    return myInt

def GetNonNegativeInteger():
    while True:
        try:
            myInt=int(input('Give a number (non-negative integer):'))
        except ValueError:
            print("Not an integer. Try again.")
            continue
        if(myInt<0):
            print("The number should be non-negative. Try Again.")
            continue
        else:
            break
    return myInt

def GetFloat():
    while True:
        try:
            myFloat=float(input('Give a number (float):'))
        except ValueError:
            print("Not a number")
            continue
        else:
            break
    return myFloat

def GetPositiveFloat():
    while True:
        try:
            myFloat=float(input('Give a number (positive float):'))
        except ValueError:
            print("Not a number")
            continue
        if(myFloat<=0):
            print("Radius should be positive. Try again.")
            continue
        else:
            break
    return myFloat

def GetNonNegativeFloat():
    while True:
        try:
            myFloat=float(input('Give a number (non-negative float):'))
        except ValueError:
            print("Not a number")
            continue
        if(myFloat<0):
            print("Radius should not be negative. Try again.")
            continue
        else:
            break
    return myFloat

def GetListOfIntegers():
    while True:
        try:
            inputString = input('Give me list of numbers (integers):')
            elements = [x.strip() for x in inputString.split(',')]
            numbersList = [int(element) for element in elements]
        except ValueError:
            print('Incorrect format of input data.')
            continue
        else:
            break
    return numbersList

def GetListOfFloats():
    while True:
        try:
            inputString = input('Give me list of numbers (floats):')
            elements = [x.strip() for x in inputString.split(',')]
            numbersList = [float(element) for element in elements]
        except ValueError:
            print('Incorrect format of input data.')
            continue
        else:
            break
    return numbersList