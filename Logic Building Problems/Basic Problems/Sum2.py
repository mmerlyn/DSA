''' Given a number n, find the sum of the first n natural numbers. '''

# Formula-based

def findSum(n):
    return n * ( n + 1 ) / 2

n = int(input("Enter n: "))
print(int(findSum(n)))