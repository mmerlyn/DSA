'''
Given two arrays a[] and b[] of size m and n respectively, the task is to determine whether b[] is a subset of a[]. Both arrays are not sorted, and elements are distinct.
'''

def isSubset(a, b):
    hash_set = set(a)

    for num in b:
        if num not in hash_set:
            return False
    return True

a = list(map(int, input("Enter a: ").split()))
b = list(map(int, input("Enter b: ").split()))
print(isSubset(a, b))