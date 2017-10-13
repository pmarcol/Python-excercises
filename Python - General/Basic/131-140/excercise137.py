"""
Write a Python program to extract single key-value pair of a dictionary in variables.
"""

"""
SOLUTION:
"""

myTestDic = {
    "key1" : 1,
    "key2" : 2,
    "key3" : 3
}

def getDicPairByKey(myKey):
    try:
        val1 = myKey
        val2 = myTestDic[myKey]
    except KeyError:
        print("No such key as \"%s\" in the dictionary." % (myKey))
        return
    else:
        return val1, val2

myTestKey1 = "key1"
myTestKey2 = "noKey"

print(getDicPairByKey(myTestKey1))
print(getDicPairByKey(myTestKey2))