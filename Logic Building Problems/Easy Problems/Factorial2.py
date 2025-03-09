''' Given the number n (n >=0), find its factorial. Factorial of n is defined as 1 x 2 x … x n. For n = 0, factorial is 1.  '''

# Recursive approach

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
    
n = int(input("Enter n: "))
print(factorial(n))