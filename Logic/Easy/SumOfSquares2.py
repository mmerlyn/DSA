''' Given n, find sum of squares of first n natural numbers. '''

# Formula based - n(n + 1)(2n + 1)/6

def summation(n):
    return (n * (n + 1) * (2 * n + 1)) / 6

n = int(input("Enter n: "))
print(summation(n))