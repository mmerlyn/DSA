''' Given two positive numbers x and y, check if y is a power of x or not. '''

# x = 10 y = 1 | 10 ^ 0 = 1
# x = 10 y = 1000 | 10 ^ 3 = 1000

# Naive Approach - Repeated Multiplication Method 
# We will check by repeated ly multiplying x until it either matches or exceeds y

def isPower(x, y):
    # The power of 1 is 1, so here if y = 1 we will return true otherwise false
    if (x == 1):
        return (y == 1)
    
    # Every wholenumber's ^ 0 is 1, so when y = 1, we will always return true
    if (y == 1):
        return True

    # Repeatedly mutliplying x with itself to until it is equal or exceeds y
    pow = x
    while(pow < y):
        pow = pow * x
    return (pow == y)


x = int(input("Enter x: "))
y = int(input("Enter y: "))
print(isPower(x, y))