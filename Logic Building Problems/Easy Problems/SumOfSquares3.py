'''Given n, find sum of squares of first n natural numbers. '''

# Recursion

def summation(n):
    if n == 1:
        return 1
    else: 
        return n ** 2 + summation(n - 1)
    
n = int(input("Enter n: "))
print(summation(n))