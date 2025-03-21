''' Given n, find sum of squares of first n natural numbers.  '''

# Naive Approach: A loop will be run from 1 to n to sum up all the squares

def summation(n):
    sum = 0
    for i in range(1, n+1):
        sum = sum + i ** 2
    return sum
    
n = int(input("Enter n: "))
print(summation(n))