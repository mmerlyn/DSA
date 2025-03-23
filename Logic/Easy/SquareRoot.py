''' Given a positive integer n, find its square root. If n is not a perfect square, then return floor of √n. '''

# Naive Approach

def findsqrt(n):
    res = 1
    while res * res <= n:
        res += 1
    return res - 1

n = int(input("Enter a number: "))
print(f"The floor square root of {n} is : {findsqrt(n)}")

# Binary Search

def findsqrt(n):
    low, high = 1, n
    res = 1

    while low <= high:
        mid = low + (high - low) // 2

        if mid * mid <= n:
            res = mid
            low = mid + 1
        else:
            high = mid - 1
    return res

# Built-in Functions

import math

def findsqrt(n):
    res = int(math.sqrt(n))
    return res