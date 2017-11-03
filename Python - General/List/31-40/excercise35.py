"""
Write a Python program to create a list by concatenating a given list which range goes from 1 to n.
Sample list : ['p', 'q']
n =5
Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']
"""

"""
SOLUTION:
"""

def myConcat(aList,reps):
    out = []
    for i in range(1, reps + 1):
        temp = [str(el) + str(i) for el in aList]
        out += temp
    return out

myList1 = ['p', 'q']
myList2 = [1, 2, 3]

print(myConcat(myList1, 3)) # ['p1', 'q1', 'p2', 'q2', 'p3', 'q3']
print(myConcat(myList2, 2)) # ['11', '21', '31', '12', '22', '32']
print(myConcat(['a'], 3))   # ['a1', 'a2', 'a3']