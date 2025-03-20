'''
Given two arrays a and b, check if they are disjoint, i.e., there is no element common between both the arrays.
'''

def areDisjoint(a, b):
    Hash_set = set(a)
    for e in b:
        if e not in set(a):
            return True
    return False

a = list(map(int, input("Enter a: ").split()))
b = list(map(int, input("Enter b: ").split()))
print(areDisjoint(a, b))