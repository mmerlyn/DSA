'''
Given two arrays, a and b of equal length. The task is to determine if the given arrays are equal or not. Two arrays are considered equal if:

Both arrays contain the same set of elements.
The arrangements (or permutations) of elements may be different.
If there are repeated elements, the counts of each element must be the same in both arrays.
'''

def checkEqual(a, b):
    n, m = len(a), len(b)
    if n != m:
        return False
    
    f = dict()

    for num in a:
        f[num] = f.get(num, 0) + 1

    for num in b:
        if num not in f:
            return False
        if f[num] == 0:
            return False
        f[num] -= 1
    return True
        
a = list(map(int, input("Enter a: ").split()))
b = list(map(int, input("Enter b: ").split()))
print(checkEqual(a, b))    