"""
Write a Python program to insert an element before each element of a list.
"""

"""
SOLUTION:
"""

def myFunc(aList,el):
    out = []
    for x in aList:
        out.append(el)
        out.append(x)
    return out

# very clever double-for solution
def origSol(aList, el):
    return [v for x in aList for v in (el, x)]

myList = [1, 3.14, "test", True]
myEl = "stop"

print(myFunc(myList, myEl)) # ["stop", 1, "stop", 3.14, "stop", "test", "stop", True]
print(origSol(myList, myEl)) # ["stop", 1, "stop", 3.14, "stop", "test", "stop", True]