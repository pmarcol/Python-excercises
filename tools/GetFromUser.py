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
            myInt=int(input('Give a number (integer):'))
        except ValueError:
            print("Not an integer. Try again.")
            continue
        if(myInt<=0):
            print("The number should be positive. Try Again.")
            continue
        else:
            break
    return myInt

def GetNonNegativetiveInteger():
    while True:
        try:
            myInt=int(input('Give a number (integer):'))
        except ValueError:
            print("Not an integer. Try again.")
            continue
        if(myInt<0):
            print("The number should be non-negative. Try Again.")
            continue
        else:
            break
    return myInt