''' Given two integers n and m (m != 0). Find the number closest to n and divisible by m. If there is more than one such number, then output the one having maximum absolute value. '''

# n = 13, m =4 | O/P: 12
# n = -15, m =6 | O/P: -18

def closestNum(n, m):
    closest = 0
    min_diff = float('inf') # positive infinity

    for i in range(n - abs(m), n + abs(m + 1)):
        if i % m == 0:
            diff = abs(n - i)

            if diff < min_diff or (diff == min_diff and abs(i) > abs(closest)):
                closest = i
                min_diff = diff
    return closest

n = int(input("Enter n: "))
m = int(input("Enter m: "))
print(closestNum(n, m))