''' Given first term (a), common difference (d) and a integer N of the Arithmetic Progression series, the task is to find Nthterm of the series. '''

# a = 2, d = 1, n = 5 | The 5th term of the series 2 3 4 5 6 ... is 6

# Formula-based tn = a + (n-1) * d

def tn_of_ap(a, d, n):
    return a + (n-1) * d

a = int(input("Enter a: "))
d = int(input("Enter d: "))
n = int(input("Enter n: "))

print(tn_of_ap(a, d, n))