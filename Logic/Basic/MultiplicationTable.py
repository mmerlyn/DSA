''' Given a number n, we need to print its table. '''

# Iterative Approach

def printTable(n):
    for i in range (1,11):
        print(f"{num} x {i} = {num * i}")

num = int(input("Enter a number: "))
printTable(num)

# Recursive Approach

def printTable(n, i = 1):
    if (i == 11):
        return
    print(f"{n} x {i} = {n * i}")
    i += 1
    printTable(n, i)