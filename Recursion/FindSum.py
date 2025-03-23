def findSum(n):
    if n == 0:
        return 0
    return n + findSum(n - 1)

n = int(input("Enter n: "))
print(findSum(n))