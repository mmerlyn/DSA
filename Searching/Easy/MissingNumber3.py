''' Naive Approach: Use 2 nested loops, where the outer one iterate from 1 to n+2, 
and inner loop iterate for each of the array arr[] elements, if the value in outer loop 
in not found in array arr[], return the value, else iterate to the next value.'''

''' Efficient Approach - Using sum of n terms formula (n(n + 1))/2. 
Compute this sum and subtract the sum of all elements in the array from it to get the missing number.'''

def missingNumber(arr):
    n = len(arr) + 1
    totalSum = sum(arr)
    expectedSum = (n * (n + 1)) // 2
    return expectedSum - totalSum

arr = list(map(int, input("Enter arr: ").split()))
print(missingNumber(arr))