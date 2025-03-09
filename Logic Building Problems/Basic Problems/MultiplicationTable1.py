''' Given a number n, we need to print its table. '''

# Iterative Approach

def printTable(n):
    for i in range (1,11):
        print(f"{num} x {i} = {num * i}")

num = int(input("Enter a number: "))
printTable(num)