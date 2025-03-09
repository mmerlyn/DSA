''' Given a positive integer n, find its square root. If n is not a perfect square, then return floor of √n. '''

# Built-in Functions

import math

def findsqrt(n):
    res = int(math.sqrt(n))
    return res

n = int(input("Enter n: "))
print(findsqrt(n))