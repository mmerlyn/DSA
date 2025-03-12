''' Given an array arr[] of size n-1 with distinct integers in the range of [1, n]. 
This array represents a permutation of the integers from 1 to n with one element missing. 
Find the missing element in the array. 
'''

''' Use an auxiliary hash hash[] to store the frequency of each element in the given array arr[].
The number with frequency 0 is the missing number
'''

def missingNumber(n):
    # Missing num is in the range of n
    n = len(arr) + 1

    # Hash array of size (n + 1)
    hashArr = [0] * (n + 1)

    # Store Frequencies
    for num in arr:
        hashArr[num] += 1
    
    for i in range(1, n + 1):
        if hashArr[i] == 0:
            return i
    
arr = list(map(int, input("Enter arr: ").split()))
print(missingNumber(arr))

'''Hash Array loop runs from 1 to n (inclusive). This means the loop runs exactly n times.
The array hashArr has n + 1 elements, but index 0 is never used, 
because the problem guarantees that numbers are in the range [1, n].
We only care about indices 1 through n, so there is no need to check hashArr[0].
'''