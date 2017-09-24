"""
 Write a Python program to add two objects if both objects are an integer type.
"""

"""
SOLUTION:
"""

def AddTwoObjectsIfInts(obj1, obj2):
    if(isinstance(obj1,int) and isinstance(obj2,int)):
        print("Both are integers, their sum is %d" % (obj1 + obj2))
        return True
    else:
        print("At least one of the objects is not integer")
        return False

varInt1 = 1
varInt2 = 2
varString = "test"
varFloat = 2.0

AddTwoObjectsIfInts(varInt1, varInt2)
AddTwoObjectsIfInts(varInt1,varString)
AddTwoObjectsIfInts(varFloat,varInt2)
AddTwoObjectsIfInts(varString,varFloat)