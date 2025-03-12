''' Given an array of size n, the task is to check if it is sorted in ascending order or not. Equal values are allowed in an array and two consecutive equal values are considered sorted. 
'''

'''Iterative Approach: We start traversing from the second element. For every element we check if it is smaller than or equal to previous element or not. At any point if we find previous element greater, we return false.'''

def checkSorting(arr):
    n = len(arr)
    if (n == 0) or (n == 1):
        return True

    else:
        for i in range(1, n):
            if arr[i-1] > arr[i]:
                return False
        return True

arr = list(map(int, input("Enter array: ").split()))
print(checkSorting(arr))