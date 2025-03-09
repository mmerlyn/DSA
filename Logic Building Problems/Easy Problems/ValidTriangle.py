''' Given three sides, check whether triangle is valid or not.  '''

# Ex: a = 7, b = 10, c = 5 | Valid

''' Def: A triangle is valid if the sum of its two sides is greater than the third side
(a + b) > c and (a + c) > b and (b + c) > a'''

def validTriangle(a, b, c):
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return False
    else:
        return True
    
a, b, c = map(int, input("Enter a, b, c: ").split())
print(validTriangle(a, b, c))