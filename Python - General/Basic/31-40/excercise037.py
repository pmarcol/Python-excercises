"""
Write a Python program to display your details like name, age, address in three different lines.
"""

"""
SOLUTION:
"""

def printDetails(name, address, age):
    print("Name: %s,\nAddress: %s,\nAge: %d" % (name, address, age))

#get name
myName = input("Give me yor name:")
#get address
myAddress = input("Give me your address:")
#get age
while True:
    try:
        myAge=int(input('Give me your age (positive integer):'))
    except ValueError:
        print("Not an integer. Try again.")
        continue
    if(myAge<0):
        print("Age should not be negative. Try again.")
        continue
    else:
        break

print(printDetails(myName, myAddress, myAge))