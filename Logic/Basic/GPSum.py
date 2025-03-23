''' A Geometric series is a series with a constant ratio between successive terms. The first term of the series is denoted by a and common ratio is denoted by r. The series looks like this :- a, ar, ar2, ar3, ar4, . . .. The task is to find the sum of such a series. '''

# GP series: a, ar, ar2. ar3 ....
# a = 1, r = 2, n = 15 | sum = 32767

# Naive Approach

a = int(input("Enter a: "))
r = int(input("Enter r: "))
n = int(input("Enter n: "))

sum = 0
i = 0
while i < n:
    sum = sum + a
    a = a * r
    i = i + 1
print(f"The sum of GP series is {sum}")

# Formula based: sum of GP series = a(1 - rn)/(1 - r)

import math

def sum_of_gp(a, r, n):
    return ( a * (1 - math.pow(r, n))) / (1 - r)

a = int(input("Enter a: "))
r = int(input("Enter r: "))
n = int(input("Enter n: "))
