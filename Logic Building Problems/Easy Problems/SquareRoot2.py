''' Given a positive integer n, find its square root. If n is not a perfect square, then return floor of √n. '''

# Binary Search

def findsqrt(n):
    low, high = 1, n
    res = 1

    while low <= high:
        mid = low + (high - low) // 2

        if mid * mid <= n:
            res = mid
            low = mid + 1
        else:
            high = mid - 1
    return res

n = int(input("Enter n: "))
print(findsqrt(n))