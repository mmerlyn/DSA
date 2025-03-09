''' Given a positive integer n, find its square root. If n is not a perfect square, then return floor of √n. '''

# Naive Approach

def findsqrt(n):
    res = 1
    while res * res <= n:
        res += 1
    return res - 1

n = int(input("Enter a number: "))
print(f"The floor square root of {n} is : {findsqrt(n)}")