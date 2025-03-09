''' Given two positive numbers x and y, check if y is a power of x or not. '''

# x = 10 y = 1 | 10 ^ 0 = 1
# x = 10 y = 1000 | 10 ^ 3 = 1000

# Logarithmic Method

import math

def isPower(x, y):
    if (x <= 0) or (y <= 0):
        return False
    
    # The power of 1 is 1, so here if y = 1 we will return true otherwise false
    if (x == 1):
        return (y == 1)
    
    # Every wholenumber's ^ 0 is 1, so when y = 1, we will always return true
    if (y == 1):
        return True
    
    res = math.log(y, x) #log y base x
    # Rounding to closest integer to avoid floating-point precision errors
    return math.isclose(res, round(res))
    

x = int(input("Enter x: "))
y = int(input("Enter y: "))
print(isPower(x, y))
    





