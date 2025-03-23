''' Given the first term a, common ratio r, and an integer N of a Geometric Progression (GP) series, the task is to find the N-th term of the series. '''

# a = 2 , r = 3, n = 5 | 5th term of this GP series is 162

# Naive Approach

a = int(input("Enter a: "))
r = int(input("Enter r: "))
n = int(input("Enter n: "))

nth_term = a
for i in range(1, n):
    nth_term *= r

print(f"The {n}th term in the series is: {nth_term}")

# Formula-based | nth term of GP series tn = a * r(n - 1)

import math

def nth_of_gp(a, r, n):
    return (a * (int)(math.pow(r, n-1)))

a = int(input("Enter a: "))
r = int(input("Enter r: "))
n = int(input("Enter n: "))







