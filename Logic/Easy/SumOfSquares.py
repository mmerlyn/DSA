''' Given n, find sum of squares of first n natural numbers.  '''

# Naive Approach: A loop will be run from 1 to n to sum up all the squares

def summation(n):
    sum = 0
    for i in range(1, n+1):
        sum = sum + i ** 2
    return sum
    
n = int(input("Enter n: "))
print(summation(n))

# Formula based - n(n + 1)(2n + 1)/6

def summation(n):
    return (n * (n + 1) * (2 * n + 1)) / 6

# Recursion

def summation(n):
    if n == 1:
        return 1
    else: 
        return n ** 2 + summation(n - 1)