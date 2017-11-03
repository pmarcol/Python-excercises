"""
Write a Python program using Sieve of Eratosthenes method for computing primes upto a specified number.
Note: In mathematics, the sieve of Eratosthenes, (Ancient Greek: κόσκινον Ἐρατοσθένους, kóskinon Eratosthénous)
one of a number of prime number sieves, is a simple, ancient algorithm for finding all prime numbers up to any given limit.
"""

"""
SOLUTION:
"""

def primes(num):
    # create original list; start from 2, because 1 is not prime
    temp = list(range(2, num + 1))
    for x in temp:
        # generate list of elements to be removed from the original list
        rems = [y for y in temp if y > x and y%x == 0]
        for rem in rems:
            temp.remove(rem)
    return temp

print(primes(10)) # [2, 3, 5, 7]
print(primes(30)) # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]