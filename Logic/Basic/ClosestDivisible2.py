''' Given two integers n and m (m != 0). Find the number closest to n and divisible by m. If there is more than one such number, then output the one having maximum absolute value. '''

# Finding by quotient

# n = 13, m =4 | O/P: 12
# n = -15, m =6 | O/P: -18

def closestNum(n, m):
    q = int(n/m)
    n1 = m * q

    if ((n * m) > 0):
        n2 = (m * (q + 1))
    else:
        n2 = (m * (q - 1))

    if (abs(n - n1) < abs(n - n2)):
        return n1
    return n2

n = int(input("Enter n: "))
m = int(input("Enter m: "))
print(closestNum(n, m))