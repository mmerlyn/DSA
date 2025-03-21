''' Given the number n (n >=0), find its factorial. Factorial of n is defined as 1 x 2 x … x n. For n = 0, factorial is 1.  '''

# Iterative Solution - we initialize result as 1 and loop from 1 to n and multiply every number with n

def factorial(n):
    res = 1

    for i in range(2, n + 1):
        res = res * i
    return res

n = int(input("Enter n: "))
print(factorial(n))