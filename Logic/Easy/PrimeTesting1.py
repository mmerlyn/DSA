''' Given a positive integer, check if the number is prime or not. A prime is a natural number greater than 1 that has no positive divisors other than 1 and itself. '''

# A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself

# Naive Method

def isPrime(n):
    #corner case
    if n <= 1: 
        return False
    
    #check from 2 to (n-1)
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n = int(input("Enter a number: "))
print("Prime") if isPrime(n) else print("Not a prime")
    
