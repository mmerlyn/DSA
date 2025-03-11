''' Given an array of positive integers arr[] of size n, the task is to find second largest distinct element in the array. If the second largest element does not exist, return -1. '''

# Naive Approach - sort, and compare the second last element with last element

def secondLargest(arr):
    arr.sort()
    n = len(arr)

    if arr[n-2] != arr[n-1] and arr[n-2] < arr[n-1]:
        return arr[n-1]
    return -1

arr = list(map(int, input("Enter the list elements: ").split()))
print(secondLargest(arr))

