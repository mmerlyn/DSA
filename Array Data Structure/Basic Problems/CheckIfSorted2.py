''' Given an array of size n, the task is to check if it is sorted in ascending order or not. Equal values are allowed in an array and two consecutive equal values are considered sorted. '''

''' Recursive Approach - The basic idea for the recursive approach:  
If size of array is zero or one, return true.
Check last two elements of array, if they are sorted, perform a recursive call with n-1 else, return false.'''

def checkSortingRec(arr, n):
    if (n == 0 or n == 1):
        return True
    return arr[n - 1] >= arr[n - 2] and checkSortingRec(arr, n - 1)

arr = list(map(int, input("Enter array numbers: ").split()))
n = len(arr)
print(checkSortingRec(arr, n))