''' Given a number n, find the sum of the first n natural numbers. '''

# Loop based

def findSum(n):
    sum = 0
    x = 1
    while x <= n:
        sum = sum + x
        x = x + 1
    return sum

n = int(input("Enter n: "))
print(findSum(n))