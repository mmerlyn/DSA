''' Given an array arr[] of size n-1 with distinct integers in the range of [1, n]. 
This array represents a permutation of the integers from 1 to n with one element missing. 
Find the missing element in the array. 
'''

''' Naive Approach: Use 2 nested loops, where the outer one iterate from 1 to n+2, 
and inner loop iterate for each of the array arr[] elements, if the value in outer loop 
in not found in array arr[], return the value, else iterate to the next value.'''

def missingNumber(arr):
    # Missing num is in the range of (1, n)
    n = len(arr) + 1

    for i in range(1, n + 1):
        found = False
        for j in range(len(arr)):
            if i == arr[j]:
                found = True
                break               
        if not found:
            return i

arr = list(map(int, input("Enter array elements: ").split()))
print(missingNumber(arr))