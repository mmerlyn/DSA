''' Given a number n, we need to print its table. '''

# Recursive Approach

def printTable(n, i = 1):
    if (i == 11):
        return
    print(f"{n} x {i} = {n * i}")
    i += 1
    printTable(n, i)

num = int(input("Enter a number: "))
printTable(num)