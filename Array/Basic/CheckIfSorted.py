''' Given an array of size n, the task is to check if it is sorted in ascending order or not. Equal values are allowed in an array and two consecutive equal values are considered sorted. '''

''' Iterative Approach - We start traversing from the second element. For every element we check if it is smaller than or equal to previous element or not. At any point if we find previous element greater, we return false.'''

def checkSorting(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return False
    return True

arr = list(map(int, input("Enter array numbers: ").split()))
print(checkSorting(arr))

''' Recursive Approach - The basic idea for the recursive approach:  
If size of array is zero or one, return true.
Check last two elements of array, if they are sorted, perform a recursive call with n-1 else, return false.'''

def checkSortingRec(arr, n):
    if (n == 0 or n == 1):
        return True
    return arr[n - 1] >= arr[n - 2] and checkSortingRec(arr, n - 1)
