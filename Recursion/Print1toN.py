# 1 to n
def printNum(n):
    if n > 0:   
        printNum(n - 1)
        print(n, end=' ')

n = int(input("Enter n: "))
# printNum(n)

# n to 1
def printNum1(n):
    if n > 0:
        print(n, end = ' ')
        printNum1(n - 1)

printNum1(n)
        